#!/usr/bin/env python3

# import operator
import argparse
import pdb


class rank:
    def __init__(self):
        parser = argparse.ArgumentParser()
        # parser.add_argument('-f', '--folds_dir', help="folds directory (e.g. folds/gold")
        requiredNamed = parser.add_argument_group('required named arguments')
        requiredNamed.add_argument('-i', '--input', help='Childes file name', required=True)
        requiredNamed.add_argument('-l', '--lang', help='Language file name', required=True)
        # parser.parse_args(['-h'])
        self.args = parser.parse_args()

    def get_counts(self, childes):
        counts ={}
        for line in childes:
            if not line.startswith("*CHI"):
                if line[0] not in ["@", "%"]:
                    for word in line.split():
                        if word not in counts:
                            counts[word] = 0
                        counts[word] += 1
        return counts

    def rank_list(self, counts, lang):
        ranked = []
        while counts != {}:
            top = max(counts, key=counts.get)
            for line in lang:
                # pdb.set_trace()
                # print(line)
                if len(line.split()) > 2:
                    if line.split()[2] == top:
                        ranked.append(line)
            pdb.set_trace()
            counts.pop(top)
            lang.seek(0)
        return ranked

    def main(self):
        childes = open(self.args.input, 'r')
        lang = open(self.args.lang, 'r')
        chi_count = self.get_counts(childes)
        ranked = self.rank_list(chi_count, lang)
        outfile = open('ranked.txt', 'w')
        for line in ranked:
            outfile.write(line)

if __name__ == '__main__':
    r = rank()
    r.main()