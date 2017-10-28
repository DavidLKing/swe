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
        # Maybe this is the best way to do it?
        self.verbs = {
            'Präsens_ich' : 'pos=V,mood=IND,tense=PRS,per=1,num=SG',
            'Präsens_du' : 'pos=V,mood=IND,tense=PRS,per=2,num=SG',
            'Präsens_er, sie, es' : 'pos=V,mood=IND,tense=PRS,per=3,num=SG',
            'Partizip II' : 'pos=V,tense=PST',
            'Präteritum_ich' : 'pos=V,mood={SBJV/COND},tense=PST,aspect=PFV,per=1,num=SG',
            'Konjunktiv II_ich' : 'pos=V,mood={SBJV/COND},tense=PST,aspect=PFV,per=1,num=SG'
            # 'Imperativ_Singular' :
        }

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
                if line[0] == '}}' and group != [] and wtype != '' and citeform != '':
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
                elif line[0] == '}}' and citeform == '':
                    # remove the entries without citation forms
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

    def conv_gend(self, gender):
        if gender == 'm':
            return 'MASC,'
        elif gender == 'f':
            return 'FEM,'
        elif gender == 'n':
            return 'NEUT,'

    def conv_num(self, num):
        if num == 'Singular' or num == 'Singular*':
            return 'num=SG'
        elif num == 'Plural':
            return 'num=PL'

    def conv_feats_n(self, feat_list, gender):
        feat = 'case='
        # print('list', feat_list)
        for word in feat_list:
            if word == 'Nominativ':
                feat += 'NOM,gen='
                feat += self.conv_gend(gender)
            elif word == "Akkusativ":
                feat += 'ACC,gen='
                feat += self.conv_gend(gender)
            elif word == 'Dativ':
                feat += 'DAT,gen='
                feat += self.conv_gend(gender)
            elif word == 'Genitiv':
                feat += 'GEN,gen='
                feat += self.conv_gend(gender)
            elif word in ['Singular', 'Singular*', 'Plural']:
                feat += self.conv_num(word)
        return feat

    def conv_feats_v(self, feat_list):
        pass

    def get_feats_n(self, gender, feat_list):
            feat_list = ' '.join(feat_list).split()
            feats = "pos=N,"
            feats += self.conv_feats_n(feat_list, gender)
            return feats

    def get_feats_v(self, feat_list):
        # print('v list', feat_list)
        feat_list = '_'.join(feat_list)
        if feat_list in self.verbs:
            feats = self.verbs[feat_list]
            return feats

    def rewrite(self, paradigms):
        for p in paradigms:
            if p[1].split('=')[0] == '|Genus':
                wtype = 'n'
                gender = p[1].split('=')[1]
                p.pop(0)
                p.pop(1)
            elif p[1].split('=')[0] == '|Präsens_ich':
                wtype = 'v'
            # pdb.set_trace()
            try:
                inf = p[-1].split()[1]
                if p[-1].split()[2] == '({{Sprache|Deutsch}})':
                    for cell in p[1:-1]:
                        if not cell.startswith("|Bild"):
                            cell = cell[1:]
                            cell = cell.split('=')
                            try:
                                assert(len(cell) >= 0)
                            except:
                                # print(cell)
                                pdb.set_trace()
                            if wtype == 'n':
                                # print(cell[0:-1])
                                feats = self.get_feats_n(gender, cell[0:-1])
                            elif wtype == 'v':
                                feats = self.get_feats_v(cell[0:-1])
                                # pdb.set_trace()
                            # if wtype != 'n':
                            #     pdb.set_trace()
                            line = '\t'.join([inf, feats, cell[-1]])
                            print(line)
                            if feats == 'pos=V,mood=IND,tense=PRS,per=3,num=SG':
                                print('\t'.join([inf, 'pos=V,mood=IND,tense=PRS,per=2,num=PL', cell[-1]]))
                    if wtype == 'v':
                        print('\t'.join([inf, 'pos=V,mood=IND,tense=PRS,per=3,num=PL', inf]))
                        print('\t'.join([inf, 'pos=V,mood=IND,tense=PRS,per=1,num=PL', inf]))


            except:
                continue
                # pdb.set_trace()
if __name__ == '__main__':
    e = extract()
    n, v, a = e.load_file()
    # e.rewrite(n)
    e.rewrite(v)
