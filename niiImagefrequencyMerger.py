import MDVcomp as mdv
import numpy as np
import sys
import json

if __name__ == '__main__':
    argNum = len(sys.argv)
    if argNum < 2:
        print "please provide argument: inPath(.json) ..."
        sys.exit(0)
    my_merger = mdv.merger()
    for i in range(1,argNum):
        my_merger.loadFreqHistogram(sys.argv[i])
    my_merger.merge()
    print json.dumps(my_merger.mergedFrequencies, sort_keys=True, indent=4, separators=(',',':'))
