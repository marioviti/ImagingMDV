import numpy as np
import MDVcomp as mdv
import json
import cv2
import setGenerator as sg

#testImage = np.array([[0,0,10,10,10],[10,0,10,10,10],[10,0,0,0,10],[10,10,10,0,10],[10,10,10,0,0]])
#print "this is a test array that represent an 2d image"
#print testImage
#sampler = mdv.sampler()
##def sample2Dbinary(self, image, thrs, patchSide)
#sampler.sample2D(testImage,[5],1,2)
#print "this dictionary represent the pattern 2x2 present in the image and their frequency"
#print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
#print "now we can proceed to binning with a factor of 10"
#sampler.binning(10)
#print json.dumps(sampler.bins, sort_keys=True, indent=4, separators=(',',':'))
#print "and take a look at which pattern went in which bin"
#print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
#print "now let's create a bank with half patterns with max entropy entries"
#sampler.maxEnthropy(0.6)
#print json.dumps(sampler.patternBank, sort_keys=True, indent=4, separators=(',',':'))
#print "now let's filter the original image"
#print sampler.threshold2D(testImage)
#print "and compare it"
#print sampler.filter2DImage(testImage)

#sampler3d = mdv.sampler()
#testImage = np.array([[[0,0],[100,45]],[[10,10],[0,0]]])
#print "this is a test array that represent an 3d image"
#print testImage
#sampler3d.sample3D(testImage,[0,30,90],2,2)
#print "this dictionary represent the pattern 2x2x2 present in the image and their frequency"
#print json.dumps(sampler3d.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))

## test sampler class
#sampler = mdv.sampler()
#testImage = np.array([[0,0,0.05,0.10,0.10],[0.10,0,0.10,0.5,10],[0.10,0,0,0,0.5],[0.15,0.10,0.10,0,0.10],[0.10,0.15,0.10,0,0]])
#sampler.sample2D(testImage,[0.1,0.5,0.10],2,3)
#sampler.maxEnthropy(1,0.5)
#
#testImage2 = np.array([[1.5,1.5,1.05,1.10,1.10],[1.50,1.1,1.10,1.5,10],[1.10,1,1,1,1.5],[1.15,1.10,1.10,1.1,1.10],[1.10,0.15,1.80,0.2,0.3]])
#sampler2 = mdv.sampler()
#sampler2.sample2D(testImage,[0.1,0.5,1.10],2,3)
#sampler2.maxEnthropy(1,0.5)
#
#print "\n" + "testImage1"
#print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
#print json.dumps(sampler.patternBank, sort_keys=True, indent=4, separators=(',',':'))
#print testImage
#print sampler.filter2DImage(testImage)
#
#print "\n" + "testImage2"
#print json.dumps(sampler2.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
#print json.dumps(sampler2.patternBank, sort_keys=True, indent=4, separators=(',',':'))
#print testImage2
#print sampler.filter2DImage(testImage2)
#
## test merger class
#merger = mdv.merger()
#merger.addFreqHistogram(sampler.freqHistogram)
#print sampler2.freqHistogram
#merger.addFreqHistogram(sampler2.freqHistogram)
#for i in merger.frequencyList:
#    print json.dumps(merger.frequencyList[i], sort_keys=True, indent=4, separators=(',',':'))


#testImage = np.array([[1.0,1.0,1.0],[1.0,1.0,1.0],[1.0,1.0,1.0]])
testImage = np.array([[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,0.0]])
sampler = mdv.sampler()
sampler.sample2D(testImage,[0.0,0.5,0.7],2,3)
testImage2 = np.array([[0.0,0.0,0.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,1.0],[1.0,1.0,1.0,0.0]])
sampler2 = mdv.sampler()
sampler2.sample2D(testImage2,[0.0,0.5,0.7],2,3)

print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
print json.dumps(sampler2.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))

merger = mdv.merger()
merger.addFreqHistogram(sampler.freqHistogram)
merger.addFreqHistogram(sampler2.freqHistogram)
merger.merge()
print json.dumps(merger.mergedFrequencies, sort_keys=True, indent=4, separators=(',',':'))





#
