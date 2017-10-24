from __future__ import print_function
import sys
import argparse
import pdb
import cPickle as pkl
import bz2 

class extract:
    def __init__(self):
        parser = argparse.ArgumentParser()
        # parser.add_argument('-f', '--folds_dir', help="folds directory (e.g. folds/gold")
        requiredNamed = parser.add_argument_group('required named arguments')
        requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)
        # parser.parse_args(['-h'])
        self.args = parser.parse_args()


    def load_file(self):
        xmlfile = self.args.input
        xf = bz2.BZ2File(xmlfile, 'r')
        line_count = 0
        nouns = []
        verbs = []
        adjec = []
        wtype = ''
        for line in xf:
            line_count += 1
            group = []
            if line.startswith('}}') and group != [] and type != '':
                if wtype = 'n':
                    nouns.append(group)
                elif wtype = 'a':
                    adjec.append(group)
                else: 
                    verbs.append(group)
                group = []
                wtype = ''
            elif line.startswith('{{Deutsch') and 


if __name__ == '__main__':
    e = extract()
    e.load_file()
