import numpy as np
import math
import operator
from . import utils
import cv2
import json

class merger:
    """
    Merges statistics attained from samplers
    """

    def __init__(self):
        self.__mergedFrequencies = self.__bins = {}
        self.__frequencyList = []

    @property
    def frequencyList(self):
        return self.__frequencyList

    @property
    def mergedFrequencies(self):
        return self.__mergedFrequencies

    @property
    def bins(self):
        return self.__bins

    #tested
    def addFreqHistogram(self, freqHistogram):
        self.__frequencyList += [freqHistogram]

    #tested
    def loadFreqHistogram(self, path):
        freqHistogram = utils.loadDictionary(path)
        self.__frequencyList += [ { int(k) : float(v) for k,v in freqHistogram.items() } ]

    #tested
    def merge(self):
        """
        after merging separate statistics reference will be lost.
        """
        overall = len(self.__frequencyList)
        keySet = set([])
        temp = 0
        for hist in self.__frequencyList:
            keySet |= set(hist.keys())
        for key in keySet:
            temp = 0
            for hist in self.__frequencyList:
                if key in hist:
                    temp += hist[key]
            temp /= float(overall)
            self.__mergedFrequencies.update({key:temp})
        self.frequencyList = [self.__mergedFrequencies]

    #tested
    def logbinning(self, binfact):
        """
        binning using the log value
        """
        historgram = self.__frequencyList[0]
        historgram = { k : math.log(v) for k,v in historgram.items() }
        self.__binfactor = binfact
        bean = maxK = minK = 0
        for patt,freq in historgram.items():
            bean = utils.binn(freq,binfact)
            if bean < minK:
                minK = bean
                if maxK == 0:
                    maxK = minK
            if bean > maxK:
                 maxk = bean
            if bean in self.__bins:
                self.__bins[bean] += 1
            else:
                self.__bins.update({bean:1})
        i = minK
        while(i<maxk):
            i += 1/float(binfact)
            if not i in self.__bins:
                self.__bins.update({i:1})

    #tested
    def binning(self, binfact):
        """
        binning
        """
        historgram = self.__frequencyList[0]
        self.__binfactor = binfact
        bean = maxK = minK = 0
        for patt,freq in historgram.items():
            bean = utils.binn(freq,binfact)
            if bean < minK:
                minK = bean
                if maxK == 0:
                    maxK = minK
            if bean > maxK:
                 maxk = bean
            if bean in self.__bins:
                self.__bins[bean] += 1
            else:
                self.__bins.update({bean:1})
        i = minK
        while(i<maxk):
            i += 1/float(binfact)
            if not i in self.__bins:
                self.__bins.update({i:1})
