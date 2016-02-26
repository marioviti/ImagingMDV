import setGenerator as sg
import MDVcomp as mdv
import json
import numpy as np

if __name__ == "__main__":
    #sg.genlineTest()
    sgg = sg.simpleGeometryGenerator()
    sgg.whiteBoard(200,200)
    sgg.drawRandomCircles(10,5)
    testImage = sgg.getImageCopy()
    #print testImage
    #sampler = mdv.sampler()
    #sampler.sample2Dbinary(testImage,127,3)
    #print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
    #sgg.showImage()
    #sgg.detectCircles()

    sampler = mdv.sampler()
    sampler.sample2D(sgg.img,[100],1,3)
    sampler.maxEnthropy(0.5, 0.5)
    print json.dumps(sampler.freqHistogram, sort_keys=True, indent=4, separators=(',',':'))
    print json.dumps(sampler.patternBank, sort_keys=True, indent=4, separators=(',',':'))
    filteredImage = sampler.filter2DImage(sgg.img)
    sgg.showImage()
    sg.showImage(filteredImage*255)
    sgg.detectCircles()
    sgg.img = filteredImage*255
    sgg.detectCircles()
