import sys
import os
import niiImaging as niiImg
import MDVcomp as mdv
import cv2
import json
import pickle
import numpy as np

if __name__ == "__main__":
    if len(sys.argv) < 3:
             print "please provide argument: inPath(.png) outPath"
             sys.exit(0)

    img = cv2.imread(sys.argv[1],0)
    edges = cv2.Canny(img,100,200)
    cv2.imwrite(os.path.join( "./", sys.argv[2]+'.png' ),edges, [cv2.IMWRITE_PNG_COMPRESSION, 0])
