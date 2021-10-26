import numpy as np
import itertools

def readTxt(dataFile):
    with open(dataFile, "r") as filestream:
        table = []
        for line in filestream:
            currentline = line.strip("\n").split(",")
            table.append(currentline)
    return table

def get_large_1_itemsets(trans_table:list, l:int) -> dict: 
    items = []
    for row in trans_table:
        for item in row:
            if item[0:l] not in items:
                items.append(item[0:l])
    items = {k:0 for k in items}
    for i, row in enumerate(trans_table):
        items_in_row = []
        for item in row:
            items_in_row.append(str(item[0:l]))
        items_keys = list(items.keys())
        for item in items_keys:
            if item in items_in_row:
                items[item] += 1
    return items

def get_filtered_t_table(trans_table:list, L:dict, l:int, minSup:list) -> list:
    minSup = minSup[l-1]
    supported_items = [k for k in L.keys() if L[k] >= minSup]
    filteredTable = []
    for i,row in enumerate(trans_table):
        items_in_row = []
        for item in row:
            c = (str(item[0:l]))
            if inSet(supported_items, c):
                items_in_row.append(item)
        if items_in_row:
            filteredTable.append(items_in_row)
    return filteredTable

def get_candidate_set(L,l):
    return list(itertools.combinations(L.keys(),l)) #2

def get_subset_support(Ck, table, minSup, l):
    subsets = {k:0 for k in Ck}
    for row in table:
        items_in_row = []
        for r in row:
            items_in_row.append(r[0:l])
        for c in Ck:
            if inSet(items_in_row,c):
                subsets[c] += 1
    return subsets

def inSet(inRow, items):
    if set(items).issubset(inRow):
        return True
    return False

def printLL(LL):
    print(" ---- "*3)
    for k,v in LL.items():
        if v:
            print("    L[",k,"]   =>",'\n')
            print(v)
            print("----\n"*2)
    
