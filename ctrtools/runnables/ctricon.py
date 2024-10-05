#!/usr/bin/env python3
import argparse
import json
from ctrtools.ctricon import CTRIcon

def main():
    parser = argparse.ArgumentParser(prog='ctricon', description='Generate a CTR ICN file')
    
    parser.add_argument('spec', help="Input JSON", type=argparse.FileType('r'))
    parser.add_argument('out', help="Output ICN", type=argparse.FileType('wb'))
    args = parser.parse_args()
    
    icn = CTRIcon.fromDict(json.load(args.spec))
    icn.toStream(args.out)


if __name__ == "__main__":
    main()