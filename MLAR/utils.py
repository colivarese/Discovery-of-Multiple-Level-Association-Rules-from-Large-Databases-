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
    items = {}
    for row in table:
        for item in row:
            if item[0] not in items:
                items[item[0]] = 0
    return items

def searchItem(table, items, size):
    for i, row in enumerate(table):
        appeared = []
        for item in row:
            c = str(item[0:size])
            if c in list(items.keys()) and c not in appeared:
                appeared.append(c)
                items[c] += 1
    return items

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
    return {item:0 for item in items}

def filterTable(table, items, minSup,size):
    if size==1:
        remainders = getRemainders(items, minSup)
    else:
        remainders = getRemainders(items, minSup)
    filteredTable = []
    for i,row in enumerate(table):
        cRow = []
        inRow = []
        for item in row:
            c = str(item[0:size])
            if c in remainders:
                cRow.append(c)
                inRow.append(item)
            continue
        if inRow:
            filteredTable.append(inRow)
    return filteredTable, minSup-1

def printTable(table):
    print("")
    for row in table:
        print(row)
    print("")
