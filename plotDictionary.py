import matplotlib.pyplot as plt
import sys
import json
import collections
import numpy as np
import math

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

if __name__ == "__main__":

    if(len(sys.argv)!=4):
        print "please provide argument: inPath(.json) xlabel ylabel"
        sys.exit(0)
    inPath = sys.argv[1]
    xlabel = sys.argv[2]
    ylabel = sys.argv[3]

    with open(inPath) as data_file:
        data = json.load(data_file)
        plot = convert(data)
        # plot = { math.log(float(k)) : math.log(float(v)) for k,v in plot.items() if float(k) > 0}
        plot = { float(k) : (float(v)) for k,v in plot.items() }
        sortedKey = sorted(plot.keys())
        print sortedKey
        yval = []
        for key in sortedKey:
            yval.append(plot[key])
        plt.bar( range(len(plot)),yval, align='center' )
        plt.xticks( range(len(plot)),sortedKey, rotation='vertical' )
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
