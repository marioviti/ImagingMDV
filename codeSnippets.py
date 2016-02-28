#### selfcompdump

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


    #cv2.imwrite(os.path.join( "./", sys.argv[2]+'_processed.png' ),filteredImage/float((2**bitdept)-1)*348, [cv2.IMWRITE_PNG_COMPRESSION, 0])

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

###Compression

# 27 KB e non comprime
#out_file = open(os.path.join( path, namefile+'_dict.txt' ), "wb")
#for i in self.__compressedDictionary:
#    arr = array.array('B',i)
#    arr.tofile(out_file)
#    out_file.write('\n')
#out_file.close()


#print "raw byte_size: " + `sys.getsizeof(self.__compressedDictionary)`

#for i in self.__compressedDictionary:
#    print i

#compressed = (zlib.compress(pickle.dumps(self.__compressedDictionary,2),9))
#print "compressed byte_size: " + `sys.getsizeof(compressed)`

#decompressed = pickle.loads(zlib.decompress(compressed))
#print "decompressed:" + '\n' + `decompressed`

#out_file = open(os.path.join( path, namefile+'_dict.mdv' ), "wb")
#out_file.write(zlib.compress(pickle.dumps(self.__compressedDictionary,2),7))
#out_file.close()

#in_file = open(os.path.join( path, namefile+'_dict.txt' ), "rb")
#todoPickle = zlib.decompress(base64.b64decode(in_file.read()))
#uncompressed = pickle.loads(todoPickle)
#if uncompressed == self.__compressedDictionary:
#    print "OK compression"

#pickle.dump( self.__compressedDictionary, open( os.path.join( path, namefile+'_dictionary.pkl' ), "wb" ))
#pickle.dump( self.__compressedOffset, open( os.path.join( path, namefile+'_offset.pkl' ), "wb" ))
#pickle.dump( self.__compressedDictionary, open( os.path.join( path, namefile+'_dictionary_2.pkl' ), "wb" ), 2 )
#pickle.dump( self.__compressedOffset, open( os.path.join( path, namefile+'_offset_2.pkl' ), "wb" ),2)
#compressed_offset = zlib.compress(cPickle.dumps(self.__compressedOffset),9)
#pickle.dump( base64.b64encode(compressed_offset), open( os.path.join( path, namefile+'_offset.zip' ), "wb" ))
#compressed_dictionary = zlib.compress(cPickle.dumps(self.__compressedDictionary),9)
#pickle.dump( base64.b64encode(compressed_dictionary), open( os.path.join( path, namefile+'_dictionary.zip' ), "wb" ))

###use multiple thresh

# cv2.imshow('image',imgthrs * (1<<16))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite(os.path.join( "./", "0100"+'.png' ), imageData[100,:,:], [cv2.IMWRITE_PNG_COMPRESSION, 0])
# cv2.imwrite(os.path.join( "./", "1100"+'.png' ), imageData[:,100,:], [cv2.IMWRITE_PNG_COMPRESSION, 0])
# cv2.imwrite(os.path.join( "./", "2100"+'.png' ), imageData[:,:,100], [cv2.IMWRITE_PNG_COMPRESSION, 0])

#   T1 weughts using *HDR values
# thrsCST = [0,50] # spinal liquid
# thrsGM = [50,150] # grey matter
# thrsWM = [150,350] # white matter
#
# DDpattDim = 3 # patch size
#
# inPath = sys.argv[1]
# imageData = niiImg.loadNiiAsCanonical(inPath)
# imageData = niiImg.loadNiiAsCanonAndCCont(inPath)
# imageData = niiImg.loadNiiAsIs(inPath)

# if(len(sys.argv)!=2):
# 	print "please provide argument: inPath(.nii or .nii.gz)"
# 	sys.exit(0)
# imageData = niiImg.loadNiiAsIsAndCCont(inPath)
#
# #
# # hist = ptb()
# # for i in range(0,imageData.shape[0]):
# #    hist.sample2D(imageData[i,:,:],thrsCST,DDpattDim)
# #    hist.sample2D(imageData[i,:,:],thrsGM,DDpattDim)
# #    hist.sample2D(imageData[i,:,:],thrsWM,DDpattDim)
#
# hist = ptb(0.001, 100)
# # x,y,z = imageData.shape
# # divide = 4
#
# # x,y,z = imageData.shape
# # divide = 8
# # stride_x = x/divide
# # stride_y = y/divide
# # stride_z = z/divide
# # hist.sample3D(imageData[0:x,0:stride_y,0:stride_z], [50, 150, 350], 3)
# # # print hist.histogram
# # print json.dumps(hist.histogram, sort_keys=True, indent=4, separators=(',',':'))
#
# hist.createLuminance3DHistogram(imageData)
# print json.dumps(hist.luminanceHistogram, sort_keys=True, indent=4, separators=(',',':'))
#
# # print hist.histogram
# # tredsample = imageData[30:33, 50:53, 20:23]
# # print tredsample
# # tredsample = niiImg.binaryThrs3D(tredsample, [180, 200, 300])
# # print tredsample
#
# # pattern = np.array([[[0, 1], [2, 3]], [[3, 2], [1, 0]]])
# # pattern = np.array([[[0, 1, 2], [3, 2, 1],[0, 1, 2]], [[0, 1, 2], [3, 2, 1],[0, 1, 2]],[[0, 1, 2], [3, 2, 1],[0, 1, 2]]])
# # pattern = np.array([[[3, 3, 3], [3, 3, 3],[3, 3, 3]], [[3, 3, 3], [3, 3, 3],[3, 3, 3]],[[3, 3, 3], [3, 3, 3],[3, 3, 3]]])
# #
# # key = niiImg.patternKey3D(pattern, 2)
# # print pattern
# # print type(key)
# # print key
# # patt = niiImg.keyPattern3D(key,3,2)
# print patt[0][0][0]

# print key
# print json.dumps(hist.histogram, sort_keys=True, indent=4, separators=(',',':'))




import matplotlib.pyplot as plt
import sys
import json
import collections
import numpy as np

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

dataPath = sys.argv[1]
xAxis = np.array(range(0,512)) # fix this to range to max index feature !!!!!!!!!!!!!!

with open(dataPath) as data_file:
    data = json.load(data_file)

# first thrs CST spinal liquid #################################################
plot0 = convert(data["0"])
orderedplot0 = collections.OrderedDict({})
for i in range(1,len(xAxis)-1):
    if `xAxis[i]` in plot0:
        orderedplot0.update({xAxis[i]:plot0[`xAxis[i]`]})

plt.bar( range(len(orderedplot0)), orderedplot0.values(), align='center' )
plt.xticks( range(len(orderedplot0)), orderedplot0.keys(), rotation='vertical' )
plt.ylabel('CST_frequencies')
plt.xlabel('pattern_index')
plt.show()
#plt.savefig( "CST_"+dataPath+".pdf", format='pdf')

## second thrs GM grey matter ###################################################
plot0 = convert(data["50"])
orderedplot0 = collections.OrderedDict({})
for i in range(1,len(xAxis)-1):
    if `xAxis[i]` in plot0:
        orderedplot0.update({xAxis[i]:plot0[`xAxis[i]`]})

plt.bar(range(len(orderedplot0)), orderedplot0.values(), align='center')
plt.xticks( range(len(orderedplot0)), orderedplot0.keys(), rotation='vertical')
plt.ylabel('GM_frequencies')
plt.show()
#plt.savefig( "GM_"+dataPath+".pdf", format='pdf')

# third thrs WM white matter ###################################################
plot0 = convert(data["150"])
orderedplot0 = collections.OrderedDict({})
for i in range(1,len(xAxis)-1):
    if `xAxis[i]` in plot0:
        orderedplot0.update({xAxis[i]:plot0[`xAxis[i]`]})

plt.bar(range(len(orderedplot0)), orderedplot0.values(), align='center')
plt.xticks( range(len(orderedplot0)), orderedplot0.keys(), rotation='vertical')
plt.ylabel('WM_frequencies')
plt.show()
#plt.savefig( "WM_"+dataPath+".pdf", format='pdf')
