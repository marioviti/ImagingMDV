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

    image = imageData[int(imageData.shape[0]/2)+4,:,:]
    sampler = mdv.sampler()
    sampler.sample2D(image,[thrsCST,thrsGM,thrsWM],bitdept,pattSideDim)
    sampler.maxEnthropy(N,W)

    cv2.imshow("show", image)
    cv2.waitKey()
    filteredImage = sampler.filter2DImage(image)

    cv2.imshow("show2", filteredImage/float((2**bitdept)-1))
    cv2.waitKey()

    sampler.encode2DAsDictionary(filteredImage)
    sampler.encode2DAsOfset(filteredImage)
    sampler.saveCompressed("./",sys.argv[2])
