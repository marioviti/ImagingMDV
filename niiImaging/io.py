import os
import math
import numpy as np
import nibabel as nib
import cv2

def allPositive(array):
    return array + abs(array.min())


def loadNiiAsCanonical(niiImagePath):
    image = nib.load(niiImagePath)
    return allPositive( niiToArray(image, True, False) )


def loadNiiAsCanonAndCCont(niiImagePath):
    image = nib.load(niiImagePath)
    return allPositive( niiToArray(image, True, True) )


def loadNiiAsIs(niiImagePath):
    image = nib.load(niiImagePath)
    return allPositive( niiToArray(image, False, False) )


def loadNiiAsIsAndCCont(niiImagePath):
    image = nib.load(niiImagePath)
    return allPositive( niiToArray(image, False, True) )


def getNumpyDataFormat(img):
    headerDataTypelabel = img.header['datatype']
    for i in range(0, len(nib.nifti1._dtdefs)):
        if nib.nifti1._dtdefs[i][0] == headerDataTypelabel:
            return nib.nifti1._dtdefs[i][2]

def niiToArray(niiImg, canonical, c_contiguos):
    dataType = getNumpyDataFormat(niiImg)
    sizeof_hdr = niiImg.header['sizeof_hdr']
    scl_slope = niiImg.header['scl_slope']
    scl_inter = niiImg.header['scl_inter']
    if math.isnan(sizeof_hdr):
        sizeof_hdr = 1
    if math.isnan(scl_slope):
        scl_slope = 1
    if math.isnan(scl_inter):
        scl_inter = 0
    if canonical:
        aligendImage = nib.as_closest_canonical(niiImg)
    else:
        aligendImage = niiImg
    INroughData = aligendImage.get_data()
    if c_contiguos and not INroughData.flags['C_CONTIGUOUS']:
        INroughData = INroughData.T
    return INroughData * scl_slope + scl_inter


def creteLossLessSlice(numpySliceData, outName, outPath):
    cv2.imwrite(os.path.join(outPath, outName + '.png'), numpySliceData, [cv2.IMWRITE_PNG_COMPRESSION, 0])


def createLossLessSliceSeries(numpySlicesData, outName, outPath):
    new_path = os.path.join(outPath, outName)
    os.makedirs(new_path)
    shape = numpySlicesData.shape
    firstImage = 0
    lastImage = shape[0]
    for extraCoord in range(firstImage, lastImage):
        cv2.imwrite(os.path.join(new_path, `extraCoord` + '.png'), numpySlicesData[extraCoord, :, :],
                    [cv2.IMWRITE_PNG_COMPRESSION, 0])
