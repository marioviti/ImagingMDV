import numpy as np
import math
import operator
from . import utils
import base64, zlib, cPickle, pickle
import os
import sys
import array
import struct

class sampler:
    """
        Sampling 2d and 3d images.
        properties:
        dict freqHistogram
            A dictionary representing the frequency relative to each pattern sampled from image
            entry : { "pattern": float frequency }
        dict patternBank
            A dictionary with all relevant pattern stored
            entry : { "pattern": float entropy }
        dict bins
            The distrubution of sammpled frequency fo the freqHistogram
            entry : { "frequency": int count }
        dict compStat
            entry : { "freqOf_Hit" : float , "pattBank_Size" : int , "pattBank_ratio" : float }
        array compressed
            entry : [[ patternkey, (x,y[,z]) , ... ] ... ]
    """

    #tested
    def __init__(self):
        self.__set = False
        self.__patternSide = self.__overall = self.__thrs = self.binfactor = 0
        self.__img = self.dim = []
        self.__freqHistogram = self.__bins = self.__patternBank = {}
        self.__compStat = { "freqOf_Hit" : 0 , "pattBank_Size" : 0 , "pattBank_ratio": 0}
        self.__compressedDictionary = []
        self.__compressedOffset = []
        self.__W = 0
        self.__N = 0

    #tested
    def initialize(self,img,patternSide,threshold,bitDepth):
        if not int(math.log(len(threshold)+1,2)) == bitDepth:
            raise ValueError("incompatible threshold and bitDepth")
        self.__bitDepth = bitDepth
        self.__img = img
        self.__threshold = threshold
        self.__shape = img.shape
        self.__patternSide = patternSide
        self.__overall = reduce(lambda x,y : (x-self.__patternSide+1)*(y-self.__patternSide+1), self.__shape)
        if self.__overall == 0:
            self.__overall = 1

    @property
    def freqHistogram(self):
        return self.__freqHistogram

    @property
    def patternBank(self):
        return self.__patternBank

    @property
    def compStat(self):
        return self.__compStat

    @property
    def compressedOffset(self):
        return self.__compressedOffset

    @property
    def compressedDictionary(self):
        return self.__compressedDictionary

    def loadPatternBank(self, path):
        self.__patternBank = { int(k) : float(v) for k,v in utils.loadDictionary(path).items() }

    #tested
    def maxEnthropy(self, percent, maxacceptance):
        patternBankval = { int(k) : utils.enthropy(v) for k, v in self.__freqHistogram.items() }
        patternBankval = sorted(patternBankval.items(), key=operator.itemgetter(1), reverse=True)
        totalLen = len(patternBankval)
        self.__N = N = int (totalLen * percent)
        self.__W = W = maxacceptance
        self.__patternBank = {}
        i = j = 0
        while j < N and i < totalLen:
            if self.__freqHistogram[patternBankval[i][0]] < maxacceptance:
                self.__patternBank.update({ patternBankval[i][0] : i })
                j+=1
            i+=1
        self.__compStat["pattBank_Size"] = i
        self.__compStat["pattBank_ratio"] = percent

    def maxSelection(self, percent, maxacceptance):
        totalLen = len(self.__freqHistogram.keys())
        self.__N = N = int (totalLen * percent)
        self.__W = W = maxacceptance
        self.__patternBank = {}
        rang = W/float(N)
        i = j = 0
        offset = .0001
        while i < N and j < 100:
            offset *= 2
            j += 1
            for patt,freq in self.__freqHistogram.items():
                if freq < rang + offset and freq > rang - offset and i < N:
                    self.__patternBank.update({ patt : i })
                    del self.freqHistogram[patt]
                    i += 1
        if j == 100:
            print "maxSelection terminated with the caution cause:\n extimated number of patterns in bank: "+ `N` +"\nactual number of patterns in bank:" + `i`
        self.__compStat["pattBank_Size"] = i
        self.__compStat["pattBank_ratio"] = percent

    #tested
    def sample2D(self, image, thrss, bitDepth, patchSide):
        """
            Sample a binary thresholded 2d image using a square patch of the specified patchSide.
        """
        self.initialize(image,patchSide,thrss,bitDepth)
        x,y = image.shape
        imageCopy = utils.multipleThrs2D(image, thrss)
        for i in range(0, x - patchSide + 1):
            for j in range(0, y - patchSide + 1):
                key = utils.patternKey(self.__bitDepth, imageCopy[i:i + patchSide, j:j + patchSide])
                if key in self.__freqHistogram:
                    self.__freqHistogram[key] += 1
                else:
                    self.__freqHistogram.update({key: 1})
        self.__freqHistogram = { k : float(v)/float(self.__overall) for k,v in self.__freqHistogram.items() }

    #tested
    def sample3D(self, image, thrss, bitDepth, patchSide):
        """
            Sample a multi level thresholded 3d image using a cubic patch of the specified patchSide.
        """
        if not len(image.shape) == 3:
            raise ValueError("must provide 2D images")
        if not int(math.log(len(thrss)+1,2)) == bitDepth :
            raise ValueError("incompatible thresholds and bitDepth")
        self.initialize(image,patchSide,thrss,bitDepth)
        x, y, z = image.shape
        imageCopy = utils.multipleThrs3D(image, thrss)
        i=j=k=0
        for i in range(0, x - self.__patternSide + 1):
            for j in range(0, y - self.__patternSide + 1):
                for k in range(0, z - self.__patternSide + 1):
                    key = utils.patternKey(self.__bitDepth, imageCopy[i:i + self.__patternSide, j:j + self.__patternSide, k:k + self.__patternSide] )
                    if key in self.__freqHistogram:
                        self.__freqHistogram[key] += 1
                    else:
                        self.__freqHistogram.update({key: 1})
        self.__freqHistogram = { k : float(v)/float(self.__overall) for k,v in self.__freqHistogram.items() }


    #tested
    def filter2DImage( self, image ):
        x, y = image.shape
        imageCopy = utils.multipleThrs2D(image, self.__threshold)
        imageSrcCopy = np.copy(imageCopy)
        imageCopy = imageCopy * 0 + int(2**self.__bitDepth) - 1
        position = {}
        #print "filter2DImage"
        fired = 0
        i = j = 0
        for i in range(0, x - self.__patternSide + 1):
            #sys.stdout.flush()
            #sys.stdout.write("\rprogress: " + `i*j/float(self.__overall)`)
            for j in range(0, y - self.__patternSide + 1):
                key = utils.patternKey(self.__bitDepth, imageSrcCopy[i:i + self.__patternSide, j:j + self.__patternSide])
                if key in self.__patternBank.keys():
                    fired += 1
                    imageCopy[i:i + self.__patternSide, j:j + self.__patternSide] = imageSrcCopy[i:i + self.__patternSide, j:j + self.__patternSide]
        self.__compStat["freqOf_Hit"] = fired / float((i-self.__patternSide)*(j-self.__patternSide))
        return imageCopy

    #testing
    def filter3DImage(self, image):
        x, y, z = image.shape
        imageCopy = utils.multipleThrs3D(image, self.__threshold)
        imageSrcCopy = np.copy(imageCopy)
        imageCopy = imageSrcCopy * 0 + 1
        i=j=k=0
        #print "filter3DImage"
        for i in range(0, x - self.__patternSide + 1):
            #sys.stdout.flush()
            #sys.stdout.write("\rprogress: " + `i*j*k/float(self.__overall)`)
            for j in range(0, y - self.__patternSide + 1):
                for k in range(0, z - self.__patternSide + 1):
                    key = utils.patternKey(self.__bitDepth, imageSrcCopy[i:i + self.__patternSide, j:j + self.__patternSide, k:k + self.__patternSide] )
                    if key in self.__patternBank.keys():
                        imageCopy[i:i + self.__patternSide, j:j + self.__patternSide, k:k + self.__patternSide] = imageSrcCopy[i:i + self.__patternSide, j:j + self.__patternSide, k:k + self.__patternSide]
        return imageCopy

    #testing
    def encode2DAsDictionary(self, image):
        """
            Use only for images after filtering, the pixel value must range in [ 0, 2^bitDepth [
        """
        x, y = image.shape
        position = {}
        for i in range(0, x - self.__patternSide + 1):
            for j in range(0, y - self.__patternSide + 1):
                key = utils.patternKey(self.__bitDepth, image[i:i + self.__patternSide, j:j + self.__patternSide])
                if key in self.patternBank:
                    id_key = self.__patternBank[key]
                    if not id_key in position:
                        position.update({id_key:len(self.__compressedDictionary)})
                        self.__compressedDictionary += [[id_key,i,j]]
                    else:
                        self.__compressedDictionary[position[id_key]] += [i,j]

    #testing
    def encode2DAsOfset(self, image):
        x, y = image.shape
        offset = 0
        zeroOffsetState = False
        for i in range(0, x):
            for j in range(0, y):
                if image[i][j] == 0 and offset == 0:
                    self.__compressedOffset += ['>']
                    offset += 1
                elif image[i][j] == 0 and offset>0:
                    offset += 1
                elif ( not image[i][j] == 0 ) and offset>0:
                    offset = 0
                    self.__compressedOffset += [offset,'<',int(image[i][j])]
                elif not image[i][j] == 0 and offset == 0:
                    self.__compressedOffset += [image[i][j]]

    #tested
    def saveCompressed( self, path ,namefile ):
        out_file = open(os.path.join( path, namefile+'_dict.mdv' ), "wb")
        out_file.write(zlib.compress(pickle.dumps(self.__compressedDictionary,2),9))
        #out_file.close()
        #for coord_list in self.compressedDictionary:
        #    out_file.write(struct.pack("I",len(coord_list)))
        #    for value in coord_list:
        #        out_file.write(struct.pack("I",value))
        out_file.close()


    #tested
    def threshold2D( self, image ):
        return utils.multipleThrs2D(image, self.__threshold)

    #tested
    def threshold3D( self, image ):
        return utils.multipleThrs3D(image, self.__threshold)


#
