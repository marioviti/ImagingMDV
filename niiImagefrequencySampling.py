import sys
import MDVcomp as mdv
import niiImaging as niiImg
import numpy as np
import json
import cv

if __name__ == "__main__":
	if(len(sys.argv)!=2):
		print "please provide argument: inPath(.nii or .nii.gz)"
		sys.exit(0)
	inPath = sys.argv[1]
	imageData = niiImg.loadNiiAsCanonical(inPath)

	sampler = mdv.sampler()
	sampler.sample3D(imageData, [0.2, 0.4, 0.8], 2, 3)
	print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
