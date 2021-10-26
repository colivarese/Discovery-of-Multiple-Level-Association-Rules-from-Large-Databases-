import csv
from treelib import Node, Tree
from utils import *
import itertools

if __name__ == '__main__':
    table = readTxt('./MLAR/transactionTable.txt')
    items = getItemSets(table=table)

    L =  {}
    for l in range(1,4):
        if l==1:
            printTable(table)
            items = searchItem(table, items,l,minSup=5)

            table, minSup = filterTable(table, items, minSup=5, size=l)
            printTable(table)
        else:
            if l > 2 :
                items = getCombinations_2(items)
                items = CombineKeys(items, l)

                items = searchItem_2(table, items, 2, 3)
                items = getCombinations_2(items)
                items = CombineKeys(items, 3)
                #items = CombineKeys(items,l)

                table, minSup = filterTable_3(table, items, 3, size=2)
                printTable(table)
                items  = searchItem_2(table, items, l, 3)


            else:
                items = getCombinations(items)

                items = searchItem(table, items, l, minSup)
                print("")
                items = CombineKeys(items,l)

                table, minSup = filterTable_2(table, items, 3, size=l)
                printTable(table)
                items = searchItem_2(table, items, l, 3)
                pass

            
