# from __future__ import print_function
import sys
import argparse
import pdb
# import cPickle as pkl
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
        # xf = bz2.BZ2File(xmlfile, 'r')
        xf = bz2.open(xmlfile, 'rt')
        line_count = 0
        nouns = []
        verbs = []
        adjec = []
        wtype = ''
        group = []
        for line in xf:
            line_count += 1
            line = line.split()
            if len(line) > 0:
                if line[0] == '}}' and group != [] and type != '':
                    if wtype == 'n':
                        nouns.append(group)
                    elif wtype == 'a':
                        adjec.append(group)
                    else:
                        verbs.append(group)
                    group = []
                    wtype = ''
                elif line[0].startswith('|') and wtype != '':
                    group.append(' '.join(line))
                elif len(line) > 2:
                    if line[2] == 'Übersicht' and line[0] == '{{Deutsch':
                        group.append(' '.join(line))
                        if line[1] == 'Substantiv':
                            wtype = 'n'
                        elif line[1] == 'Verb':
                            wtype = 'v'
                        else:
                            wtype = 'a'
        print("Total lines", line_count)
        print("Total nouns", len(nouns))
        print("Total verbs", len(verbs))
        print("Total adjectives", len(adjec))


if __name__ == '__main__':
    e = extract()
    e.load_file()
