#!/usr/bin/env python3

import sys
import argparse
import pdb
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
        citeform = ''
        for line in xf:
            line_count += 1
            line = line.split()
            if len(line) > 0:
                # if line[0] == '}}' and group != [] and wtype != '':
                # TODO this is a hack to work on the test file
                if line[0] == '}}' and group != [] and wtype != '':
                    group.append(citeform)
                    if wtype == 'n':
                        nouns.append(group)
                    elif wtype == 'a':
                        adjec.append(group)
                    # elif wtype == 'v':
                    else:
                        verbs.append(group)
                    # ignore the rest
                    group = []
                    wtype = ''
                    citeform = ''
                elif line[0] == '==' and line[-1] == '==':
                    citeform = ' '.join(line)
                elif line[0].startswith('|') and wtype != '':
                    group.append(' '.join(line))
                elif len(line) > 2:
                    if line[2] == 'Übersicht' and line[0] == '{{Deutsch':
                        group.append(' '.join(line))
                        if line[1] == 'Substantiv':
                            wtype = 'n'
                        elif line[1] == 'Verb':
                            wtype = 'v'
                        elif line[1] == 'Adjektiv':
                            wtype = 'a'
                        # ignore Nachname/Vorname Übersicht type tables
                        else:
                            wtype = ''
        print("Total lines", line_count)
        print("Total nouns", len(nouns))
        print("Total verbs", len(verbs))
        print("Total adjectives", len(adjec))
        return nouns, verbs, adjec

    def rewrite_verb(self, paradigms):
        for p in paradigms:
            inf = p[-1].split()[1]
            assert(p[-1].split()[2] == '({{Sprache|Deutsch}})')
            for cell in p[1:-1]:
                cell = cell.split('=')
                try:
                    assert(len(cell) >= 0)
                except:
                    print(cell)
                    pdb.set_trace()
                line = '\t'.join([inf, '-'.join(cell[0:-1])[1:], cell[-1]])
                print(line)

if __name__ == '__main__':
    e = extract()
    n, v, a = e.load_file()
    e.rewrite_verb(v)
