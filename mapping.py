import sys

class mapping:
    def __init__(self):
        parser = argparse.ArgumentParser()
        # parser.add_argument('-f', '--folds_dir', help="folds directory (e.g. folds/gold")
        requiredNamed = parser.add_argument_group('required named arguments')
        requiredNamed.add_argument('-i', '--input', help='Input file name', required=True)
        # parser.parse_args(['-h'])
        self.args = parser.parse_args()

    def nouns(self, gender, string):
        pass

    def verbs(self):
        pass

    def main(self, file):
        for line in open(file, 'r').readlines():


if __name__ == '__main__':
    m = mapping()



"""
pos=ADJ,case=ACC,comp=CMPR,gen=FEM,num=SG
pos=ADJ,case=ACC,comp=CMPR,gen=MASC,num=SG
pos=ADJ,case=ACC,comp=CMPR,gen=NEUT,num=SG
pos=ADJ,case=ACC,comp=CMPR,num=PL
pos=ADJ,case=ACC,comp=SPRL,gen=FEM,num=SG
pos=ADJ,case=ACC,comp=SPRL,gen=MASC,num=SG
pos=ADJ,case=ACC,comp=SPRL,gen=NEUT,num=SG
pos=ADJ,case=ACC,comp=SPRL,num=PL
pos=ADJ,case=ACC,gen=FEM,num=SG
pos=ADJ,case=ACC,gen=MASC,num=SG
pos=ADJ,case=ACC,gen=NEUT,num=SG
pos=ADJ,case=ACC,num=PL
pos=ADJ,case=DAT,comp=CMPR,gen=FEM,num=SG
pos=ADJ,case=DAT,comp=CMPR,gen=MASC,num=SG
pos=ADJ,case=DAT,comp=CMPR,gen=NEUT,num=SG
pos=ADJ,case=DAT,comp=SPRL,gen=FEM,num=SG
pos=ADJ,case=DAT,comp=SPRL,gen=MASC,num=SG
pos=ADJ,case=DAT,comp=SPRL,gen=NEUT,num=SG
pos=ADJ,case=DAT,gen=FEM,num=SG
pos=ADJ,case=DAT,gen=MASC,num=SG
pos=ADJ,case=DAT,gen=NEUT,num=SG
pos=ADJ,case=GEN,comp=CMPR,gen=FEM,num=SG
pos=ADJ,case=GEN,comp=CMPR,gen=MASC,num=SG
pos=ADJ,case=GEN,comp=CMPR,gen=NEUT,num=SG
pos=ADJ,case=GEN,comp=CMPR,num=PL
pos=ADJ,case=GEN,comp=SPRL,gen=FEM,num=SG
pos=ADJ,case=GEN,comp=SPRL,gen=MASC,num=SG
pos=ADJ,case=GEN,comp=SPRL,gen=NEUT,num=SG
pos=ADJ,case=GEN,comp=SPRL,num=PL
pos=ADJ,case=GEN,gen=FEM,num=SG
pos=ADJ,case=GEN,gen=MASC,num=SG
pos=ADJ,case=GEN,gen=NEUT,num=SG
pos=ADJ,case=GEN,num=PL
pos=ADJ,case=NOM,comp=CMPR,gen=FEM,num=SG
pos=ADJ,case=NOM,comp=CMPR,gen=MASC,num=SG
pos=ADJ,case=NOM,comp=CMPR,gen=NEUT,num=SG
pos=ADJ,case=NOM,comp=CMPR,num=PL
pos=ADJ,case=NOM,comp=SPRL,gen=FEM,num=SG
pos=ADJ,case=NOM,comp=SPRL,gen=MASC,num=SG
pos=ADJ,case=NOM,comp=SPRL,gen=NEUT,num=SG
pos=ADJ,case=NOM,comp=SPRL,num=PL
pos=ADJ,case=NOM,gen=FEM,num=SG
pos=ADJ,case=NOM,gen=MASC,num=SG
pos=ADJ,case=NOM,gen=NEUT,num=SG
pos=ADJ,case=NOM,num=PL
pos=ADJ,comp=CMPR
pos=ADJ,comp=SPRL,per=3,num=SG
pos=N,case=ACC,gen=FEM,num=PL
pos=N,case=ACC,gen=FEM,num=SG
pos=N,case=ACC,gen=MASC,num=PL
pos=N,case=ACC,gen=MASC,num=SG
pos=N,case=ACC,gen=NEUT,num=PL
pos=N,case=ACC,gen=NEUT,num=SG
pos=N,case=DAT,gen=FEM,num=PL
pos=N,case=DAT,gen=FEM,num=SG
pos=N,case=DAT,gen=MASC,num=PL
pos=N,case=DAT,gen=NEUT,num=PL
pos=N,case=GEN,gen=FEM,num=PL
pos=N,case=GEN,gen=FEM,num=SG
pos=N,case=GEN,gen=MASC,num=PL
pos=N,case=GEN,gen=MASC,num=SG
pos=N,case=GEN,gen=MASC,num=SG,alt=LGSPEC1
pos=N,case=GEN,gen=NEUT,num=PL
pos=N,case=GEN,gen=NEUT,num=SG
pos=N,case=GEN,gen=NEUT,num=SG,alt=LGSPEC1
pos=N,case=NOM,gen=FEM,num=PL
pos=N,case=NOM,gen=FEM,num=SG
pos=N,case=NOM,gen=MASC,num=PL
pos=N,case=NOM,gen=MASC,num=SG
pos=N,case=NOM,gen=NEUT,num=PL
pos=N,case=NOM,gen=NEUT,num=SG
pos=V,finite=NFIN
pos=V,mood=IND,tense=PRS,per=1,num=PL
pos=V,mood=IND,tense=PRS,per=1,num=SG
pos=V,mood=IND,tense=PRS,per=2,num=PL
pos=V,mood=IND,tense=PRS,per=2,num=SG
pos=V,mood=IND,tense=PRS,per=3,num=PL
pos=V,mood=IND,tense=PRS,per=3,num=SG
pos=V,mood=IND,tense=PST,aspect=PFV,per=1,num=PL
pos=V,mood=IND,tense=PST,aspect=PFV,per=1,num=SG
pos=V,mood=IND,tense=PST,aspect=PFV,per=2,num=PL
pos=V,mood=IND,tense=PST,aspect=PFV,per=2,num=SG
pos=V,mood=IND,tense=PST,aspect=PFV,per=3,num=PL
pos=V,mood=IND,tense=PST,aspect=PFV,per=3,num=SG
pos=V,mood={OPT/SBJV},tense=PRS,per=1,num=PL
pos=V,mood={OPT/SBJV},tense=PRS,per=1,num=SG
pos=V,mood={OPT/SBJV},tense=PRS,per=2,num=PL
pos=V,mood={OPT/SBJV},tense=PRS,per=2,num=SG
pos=V,mood={OPT/SBJV},tense=PRS,per=3,num=PL
pos=V,mood={OPT/SBJV},tense=PRS,per=3,num=SG
pos=V,mood={SBJV/COND},tense=PST,aspect=PFV,per=1,num=PL
pos=V,mood={SBJV/COND},tense=PST,aspect=PFV,per=1,num=SG
pos=V,mood={SBJV/COND},tense=PST,aspect=PFV,per=2,num=PL
pos=V,mood={SBJV/COND},tense=PST,aspect=PFV,per=2,num=SG
pos=V,mood={SBJV/COND},tense=PST,aspect=PFV,per=3,num=PL
pos=V,mood={SBJV/COND},tense=PST,aspect=PFV,per=3,num=SG
pos=V,tense=PRS
pos=V,tense=PST

"""