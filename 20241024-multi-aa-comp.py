#packages
import numpy as np
import pandas as pd
import jellyfish
import multiprocessing as mp
#read data
#u2os_AA = pd.read_csv('/nas/longleaf/home/seli/imported-files/U2OS.pacbio_AA.csv')
#HG_AA = pd.read_csv('/nas/longleaf/home/seli/imported-files/telos.AA.csv')

u2os_AA = pd.read_csv('U2OS.pacbio_AA.csv')
HG_AA = pd.read_csv('telos.AA.csv')

# mutation frequency
# end goal: list of subtelo ORFS & 30 AA of telomere
# 20 AA of RV is good for telos
# seq to first stop codon

# defining class
class results:
    def __init__(self, s1n, s1sq, s2n, s2sq, scr):
        self.s1n = s1n #seq1 name
        self.s1sq = s1sq #seq1
        self.s2n = s2n #seq2 name
        self.s2sq = s2sq #seq2
        self.scr = scr #score
    def as_dict(self):
        return {'Seq1-Name':self.s1n,'Seq2-Name':self.s2n,
                'Seq1':self.s1sq,'Seq2':self.s2sq,'Score':self.scr}

# multiprocessing time
comp_list=[]
# work function: what should each fella do?
def work_func(s1,s2):
    score=jellyfish.damerau_levenshtein_distance(s1['AA-Frame1'], s2['AA-Frame1'])
    result = results(s1['Name']+' Frame 1',
                     s1['AA-Frame1'],
                     s2['Name']+' Frame 1',
                     s2['AA-Frame1'],
                     score)
    return result

def log_result(result):
    comp_list.append(result)
    
#comparison
def compare_aminoacids(ser1,ser2):
    pool = mp.Pool()
    for i, s1 in  ser1.iterrows():
        for j, s2 in ser2.iterrows():
            pool.apply_async(work_func, args = (s1,s2),callback=log_result)
    pool.close()
    pool.join()
    df = pd.DataFrame([vars(x) for x in comp_list])
    return df

if __name__ == "__main__":
    comparison1 = compare_aminoacids(HG_AA, u2os_AA)
    comparison1.to_csv('HG_U2OS_comp-Frame1.csv')
#comparison1.to_csv('/nas/longleaf/home/seli/imported-files/HG_SELF_comp-MULTITEST.csv')
#comparison2 = compare_aminoacids(u2os_AA, HG_AA)
#comparison2.to_csv('/nas/longleaf/home/seli/imported-files/HG_U2OS_comp-FRAME1.csv')
