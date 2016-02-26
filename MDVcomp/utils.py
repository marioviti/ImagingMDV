import math
import json
import collections
import numpy as np

#tested
def enthropy(p):
    return -1* p * math.log(p,2)

#tested
def binn(freq, binfact):
    return math.floor(float(freq)*float(binfact)) * float(1)/float(binfact)
    

#tested
def keyPattern( pattshape, bitDepth, key ):
    """
        Given a key number returns a pattern in the specified pattshape, bitDepth
    """
    flatdim = reduce(lambda x,y: x*y, pattshape)
    pattern = np.array( range(0, flatdim) ) * 0
    if key == int((2**bitDepth)**flatdim) - 1:
        pattern.shape = pattshape
        return pattern + (int(2**bitDepth) - 1)
    if key == 0:
        pattern.shape = pattshape
        return  pattern * 0
    for i in range(0, len(pattern)):
        pattern[i] = key % int(2**bitDepth)
        key >>= bitDepth
    pattern.shape = pattshape
    return pattern

#tested
def patternKey( bitDepth, pattern ):
    """
        Given a pattern returns a key in the specified bitDepth
    """
    flatdim = reduce(lambda x,y: x*y, pattern.shape)
    flatpatt = pattern.flatten()
    acc = 0
    for i in range(0,flatdim):
        acc += (1 << ((i) * bitDepth)) * int(flatpatt[i])
    return acc

#tested
def multipleThrs2D(src, thrss):
    x, y = src.shape
    thrss.sort()
    image = np.copy(src)
    for i in range(0, x):
        for j in range(0, y):
            if image[i][j] < thrss[0]:
                image[i][j] = 0
            elif image[i][j] >= thrss[len(thrss) - 1]:
                image[i][j] = len(thrss)
            else:
                for t in range(0, len(thrss)-1):
                    if image[i][j] >= thrss[t] and image[i][j] < thrss[t+1]:
                        image[i][j] = t+1
    return image

#tested
def multipleThrs3D(src, thrss):
    x, y, z = src.shape
    image = np.copy(src)
    for i in range(0, x):
        for j in range(0, y):
            for k in range(0, z):
                if image[i][j][k] < thrss[0]:
                    image[i][j][k] = int(0)
                elif image[i][j][k] >= thrss[len(thrss) - 1]:
                    image[i][j][k] = int(len(thrss))
                else:
                    for t in range(0, len(thrss)-1):
                        if image[i][j][k] >= thrss[t] and image[i][j][k] < thrss[t+1]:
                            image[i][j][k] = int( t+1 )
    return image

#tested
def createLuminance3DHistogram(image):
    luminanceHistogram = {}
    luminance = 0
    x,y,z = image.shape
    for i in range(0, x):
        for j in range(0, y):
            for k in range(0, z):
                luminance = int(image[i][j][k])
                if luminance in luminanceHistogram:
                    luminanceHistogram[luminance] += 1
                else:
                    luminanceHistogram.update({luminance:1})
    return luminanceHistogram

def entropy(count, overrall):
    p = count/overrall
    return (-1)*p*math.log(2,p)

def loadDictionary(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data
