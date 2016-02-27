import sys
import os
import niiImaging as niiImg
import MDVcomp as mdv
import cv2
import json
import pickle
import numpy as np
from scipy.fftpack import dct as dctrans
import zlib, cPickle

#####################################

# T1 weughts
thrsCST = 0.4#150# # spinal liquid
thrsGM = 0.5#200# # grey matter
thrsWM = 0.8#280# # white matter

# Quantization
pattSideDim = 3 # patch size
bitdept = 2 # bit depth

# Compression parameters
N = 0.05
W = 0.01

######################################

if __name__ == "__main__":
    if len(sys.argv) < 3:
             print "please provide argument: inPath(.nii) outPath"
             sys.exit(0)

    inPath = sys.argv[1]
    imageData = niiImg.loadNiiAsCanonical(inPath)
    #imageData = niiImg.loadNiiAsCanonAndCCont(inPath)
    #imageData = niiImg.loadNiiAsIs(inPath)
    #imageData = niiImg.loadNiiAsIsAndCCont(inPath)

    image = imageData[int(imageData.shape[0]/2)+6,:,:]
    #image = cv2.imread(sys.argv[1],0)
    sampler = mdv.sampler()
    sampler.sample2D(image,[thrsCST,thrsGM,thrsWM],bitdept,pattSideDim)
    sampler.maxEnthropy(N,W)
    #print "num of patterns " + `acc`
    #print json.dumps(sampler.patternBank, sort_keys=True, indent=4, separators=(',',':'))
    cv2.imshow("show", image)
    cv2.waitKey()
    #cv2.imwrite(os.path.join( "./", sys.argv[2]+'.png' ),image*348, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    filteredImage = sampler.filter2DImage(image)

    cv2.imshow("show2", filteredImage/float((2**bitdept)-1))
    cv2.waitKey()

    sampler.encode2DAsDictionary(filteredImage)
    sampler.encode2DAsOfset(filteredImage)
    sampler.saveCompressed("./",sys.argv[2])

    ## print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
    ## print json.dumps(sampler.compStat, sort_keys=True, indent=4, separators=(',',':'))
    ## print json.dumps(sampler.compressed, sort_keys=True, indent=4, separators=(',',':'))
    ## print sampler.compressed

    #sampler.encode2DAsDictionary(filteredImage)
    #sampler.encode2DAsOfset(filteredImage)
    ##pickle.dump(zlib.compress(cPickle.dumps(sampler.compressedDictionary,cPickle.HIGHEST_PROTOCOL),9), open( os.path.join( "./", sys.argv[2]+'.pkl' ), "wb" ),2)
    #pickle.dump( zlib.compress(cPickle.dumps(sampler.compressedDictionary,cPickle.HIGHEST_PROTOCOL),7), open( os.path.join( "./", sys.argv[2]+'.pkl' ), "wb" ))

    #test = sampler.compressedDictionary
    #comp = zlib.compress(cPickle.dumps(sampler.compressedDictionary,cPickle.HIGHEST_PROTOCOL),9)
    #print len(comp)
    #test2 = cPickle.loads(zlib.decompress(comp))


    cv2.imwrite(os.path.join( "./", sys.argv[2]+'_processed.png' ),filteredImage/float((2**bitdept)-1)*348, [cv2.IMWRITE_PNG_COMPRESSION, 0])

    ##dct = np.copy(image)
    ##trans = dctrans(dct)
    #cv2.imshow("showtrans", trans)
    #cv2.waitKey()

    #imageCenter = niiImg.binaryThrs2D(imageData[int(imageData.shape[0]/2),:,:],thrsCST) * (1<<16)
    #cv2.imwrite(os.path.join( "./", "centerCST"+'.png' ),imageCenter, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    ##imageData = niiImg.loadNiiAsCanonical(inPath)
    #imageCenter = niiImg.binaryThrs2D(imageData[int(imageData.shape[0]/2),:,:],thrsGM) * (1<<16)
    #cv2.imwrite(os.path.join( "./", "centerGM"+'.png' ), imageCenter, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    ##imageData = niiImg.loadNiiAsCanonical(inPath)
    #imageCenter = niiImg.binaryThrs2D(imageData[int(imageData.shape[0]/2),:,:],thrsWM) * (1<<16)
    #cv2.imwrite(os.path.join( "./", "centerWM"+'.png' ), imageCenter, [cv2.IMWRITE_PNG_COMPRESSION, 0])
