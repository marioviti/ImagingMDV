import niiImaging as niiImg
import MDVcomp as mdv
import numpy as np
import json
import sys
import cv

if __name__ == "__main__":

    if(len(sys.argv)!=2):
        print "please provide argument: inPath(.nii or .nii.gz)"
        sys.exit(0)
    inPath = sys.argv[1]
    imageData = niiImg.loadNiiAsIsAndCCont(inPath)

    print json.dumps(mdv.createLuminance3DHistogram(imageData), sort_keys=True, indent=4, separators=(',',':'))
