import numpy as np
import itertools

def readTxt(dataFile):
    with open(dataFile, "r") as filestream:
        table = []
        for line in filestream:
            currentline = line.strip("\n").split(",")
            table.append(currentline)
    return table

def getItemSets(table):
    items = []
    for row in table:
        for item in row:
            if item[0] not in items:
                items.append(item[0])
    return items

def searchItem(table, items, size,minSup):
    items = {k:0 for k in items}
    for i, row in enumerate(table):
        appeared = []
        for item in row:
            c = str(item[0:size])
            if c in items and c not in appeared:
                appeared.append(c)
                items[c] += 1
    print(items)
    items = getRemainders(items,minSup)
    return items

def searchItem_2(table, items, size,minSup):
    items = {k:0 for k in items}
    for i, row in enumerate(table):
        appeared = []
        inRow = []
        for item in row:
            c = str(item[0:size])
            inRow.append(c)
        for i in items:
            i = list(i)
            if set(i).issubset(inRow):
                items[tuple(i)] += 1
        if c in items and c not in appeared:
            appeared.append(c)
            items[c] += 1
    print(items)
    tmp = len(list(items.keys()))
    if tmp == 1:
        minSup = 2
    items = getRemainders(items,minSup+1)
    return [list(i) for i in items]

def getRemainders(items, minSup):
    return [k for k in items.keys() if items[k] >= minSup]

def getCombinations(remainders):
    s = ''
    for r in remainders:
        s += r
    combinations = list(itertools.product(s, s))
    items = []
    for comb in combinations:
        s = ''
        for c in comb:
            s += c
        items.append(s)
    return items

def filterTable(table, items, minSup,size):
    filteredTable = []
    for i,row in enumerate(table):
        cRow = []
        inRow = []
        for item in row:
            c = str(item[0:size])
            if sublist(c,items):
                cRow.append(item)
            continue
        if cRow:
            filteredTable.append(cRow)
    return filteredTable, minSup-1


def filterTable_2(table, items, minSup,size):
    filteredTable = []
    for i,row in enumerate(table):
        cRow = []
        inRow = []
        for item in row:
            c = str(item[0:size])
            inRow.append(c)
            continue
        if inSet(inRow,items):
            filteredTable.append(row)
    return filteredTable, minSup-1

def filterTable_3(table, items, minSup,size):
    filteredTable = []
    for i,row in enumerate(table):
        cRow = []
        inRow = []
        for item in row:
            c = str(item[0:size])
            if c in items[0]:
                inRow.append(str(item[0:size+1]))
            continue
        filteredTable.append(inRow)
    return filteredTable, minSup-1

def printTable(table):
    print("")
    for row in table:
        print(row)
    print("")

def inSet(inRow, items):
    for i in items:
        i = list(i)
        if set(i).issubset(inRow):
            return True
    return False
    
    

def sublist(lst1, lst2):
    return set(lst1) <= set(lst2)

def CombineKeys(items,size):
    combinations = list(itertools.combinations(items,size))
    #return {k:0 for k in combinations}
    return combinations

def getCombinations_2(remainders):
    rems = []
    for r in remainders:
        for i in r:
            if i not in rems:
                rems.append(i)
    return rems


