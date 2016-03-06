import MDVcomp as mdv
import sys
import json

def main():
    if len(sys.argv) < 3:
        print "please provide argument: inPath(.json) binningFactor"
        sys.exit(0)
    inPath = sys.argv[1]
    binningFactor = sys.argv[2]
    binner = mdv.merger()
    binner.loadFreqHistogram(inPath)
    binner.merge
    binner.logbinning(binningFactor)
    print json.dumps(binner.bins, sort_keys=True, indent=4, separators=(',',':'))

if __name__ == '__main__':
    main()
