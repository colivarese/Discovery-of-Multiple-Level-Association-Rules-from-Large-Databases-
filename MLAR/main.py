import csv
from treelib import Node, Tree
from utils import *
import itertools
from fun import *

if __name__ == '__main__':
    table = readTxt('./MLAR/transactionTable.txt')
    items = getItemSets(table=table)

    LL = {}
    minSup = [4,3,3]
    minSup.append(minSup[-1])
    for l in range(1,4):
        if l==1:
            LL[(l,1)] = get_large_1_itemsets(trans_table=table, l=l)
            table = get_filtered_t_table(trans_table=table, L=LL[(l,1)], l=l, minSup=minSup)
        else:
            LL[(l,1)] = get_large_1_itemsets(trans_table=table, l=l)
        for k in range(2,4):
            candidate_set = get_candidate_set(LL[(l,k-1)])
            subsets = get_subset_support(Ck = candidate_set, table=table, minSup=minSup[l], l=l)
            LL[(l,k)] = {k:v for k,v in subsets.items() if v >= minSup[l]}

    printLL(LL)


            
