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
thrsCST = 0.4 # spinal liquid
thrsGM = 0.5 # grey matter
thrsWM = 0.8 # white matter

# Quantization
pattSideDim = 3 # patch size
bitdept = 2 # bit depth

# Compression parameters
N = 0.005
W = 0.0005

######################################

if __name__ == "__main__":
    if len(sys.argv) < 4:
             print "please provide argument: inPath(.nii) outPath pattbank"
             sys.exit(0)

    inPath = sys.argv[1]
    outPath = sys.argv[2]
    pathpattern = sys.argv[3]
    imageData = niiImg.loadNiiAsCanonical(inPath)
    sampler = mdv.sampler()
    sampler.sample3D(imageData, [thrsCST, thrsGM, thrsWM], bitdept, pattSideDim)
    sampler.maxEnthropy(N,W)
    copyData = sampler.filter3DImage(imageData)
    niiImg.createLossLessSliceSeries(copyData/float((2**bitdept)-1)*348, "prova", outPath)
