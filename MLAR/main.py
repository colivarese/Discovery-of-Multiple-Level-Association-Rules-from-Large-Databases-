import csv
from treelib import Node, Tree
from utils import *
import itertools

if __name__ == '__main__':
    table = readTxt('./MLAR/transactionTable.txt')
    items = getItemSets(table=table)
    
    #items = searchItem(table, items,1)

    L =  {}
    for l in range(1,4):
        if l==1:
            items = searchItem(table, items,l)
            print("")
            print(items)
            table, minSup = filterTable(table, items, minSup=5, size=l)
            printTable(table)
        else:
            remainders = getRemainders(items,minSup)
            remainders = getCombinations(remainders)
            print("")

            items = searchItem(table, remainders, l)
            print(items)
            print("")

            table, minSup = filterTable(table, items, minSup, size=l)
            printTable(table)
            pass
            
