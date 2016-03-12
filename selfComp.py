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
thrsCST = 0.2#150# # spinal liquid
thrsGM = 0.4#200# # grey matter
thrsWM = 0.6#280# # white matter

# Quantization
pattSideDim = 3 # patch size
bitdept = 2 # bit depth

# Compression parameters
N = 0.05
W = 0.3

######################################

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "please provide argument: inPath(.nii) outPath"
        sys.exit(0)
    inPath = sys.argv[1]
    imageData = niiImg.loadNiiAsCanonical(inPath)

    #image = imageData[int(imageData.shape[0]/2)+10,:,:] # RL
    #image = imageData[:,int(imageData.shape[1]/2),:] #AP
    image = imageData[:,:,int(imageData.shape[2]/2)+50] #SI
    cv2.imwrite(os.path.join( "./", sys.argv[2]+"_originale"+'.png' ), image*180, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imshow("show", image)
    cv2.waitKey()
    imageThrs = mdv.utils.multipleThrs2D(image, [thrsCST,thrsGM,thrsWM])
    cv2.imshow("show", imageThrs/float((2**bitdept)-1))
    cv2.waitKey()
    sampler = mdv.sampler()
    sampler.sample2D(image,[thrsCST,thrsGM,thrsWM],bitdept,pattSideDim)
    sampler.maxSelection(N,W)
    #sampler.maxEnthropy(N,W)
    filteredImage = sampler.filter2DImage(image)
    cv2.imshow("show2", filteredImage/float((2**bitdept)-1))
    cv2.waitKey()
    #print sampler.compStat
    sampler.encode2DAsDictionary(filteredImage)
    sampler.encode2DAsOfset(filteredImage)
    sampler.encodeWhiteSpace(image)
    #print "size of compressedDictionary in main memory:" + `sys.getsizeof(sampler.compressedDictionary)`
    sampler.saveCompressed("./",sys.argv[2])


    cv2.imwrite(os.path.join( "./", sys.argv[2]+"_thrs"+'.png' ), imageThrs*100, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imwrite(os.path.join( "./", sys.argv[2]+"_comp"+'.png' ), filteredImage*100, [cv2.IMWRITE_PNG_COMPRESSION, 0])

    #print json.dumps(sampler.patternBank, sort_keys=True, indent=1, separators=(',',':'))
    #print json.dumps(sampler.compStat, sort_keys=True, indent=1, separators=(',',':'))
