import os
import sys
import niiImaging as niiImg

if(len(sys.argv)!=3):
	print "please provide argument: inPath(.nii or .nii.gz) outPath"
	sys.exit(0)

inPath = sys.argv[1]
outName = os.path.basename(os.path.normpath(sys.argv[1]))
outPath = sys.argv[2]
imageData = niiImg.loadNiiAsCanonical(inPath)
niiImg.createLossLessSliceSeries(imageData, outName, outPath)
