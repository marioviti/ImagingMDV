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

    image = imageData[int(imageData.shape[0]/2)+10,:,:]
    sampler = mdv.sampler()
    sampler.sample2D(image,[thrsCST,thrsGM,thrsWM],bitdept,pattSideDim)
    sampler.maxSelection(N,W)
    cv2.imshow("show", image)
    cv2.waitKey()
    filteredImage = sampler.filter2DImage(image)
    cv2.imshow("show2", filteredImage/float((2**bitdept)-1))
    cv2.waitKey()
    #print sampler.compStat
    sampler.encode2DAsDictionary(filteredImage)
    sampler.encode2DAsOfset(filteredImage)
    #print "size of compressedDictionary in main memory:" + `sys.getsizeof(sampler.compressedDictionary)`
    sampler.saveCompressed("./",sys.argv[2])

    print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
