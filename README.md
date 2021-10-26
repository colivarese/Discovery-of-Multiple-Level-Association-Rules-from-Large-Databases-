# Discovery-of-Multiple-Level-Association-Rules-from-Large-Databases-
Find association rules with hierarchies, based on: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.64.3214&amp;rep=rep1&amp;type=pdf

Example in the paper:

    L[ (1, 1) ]   => 

    {'1': 5, '2': 5, '3': 3, '4': 3, '5': 2, '7': 1}
    ----
    ----

        L[ (1, 2) ]   => 

    {('1', '2'): 4}
    ----
    ----

        L[ (2, 1) ]   => 

    {'11': 5, '12': 4, '21': 4, '22': 4}
    ----
    ----

        L[ (2, 2) ]   => 

    {('11', '12'): 4, ('11', '21'): 3, ('11', '22'): 4, ('12', '22'): 3, ('21', '22'): 3}
    ----
    ----

        L[ (3, 1) ]   => 

    {'111': 4, '121': 2, '211': 4, '221': 3, '222': 1, '112': 1, '122': 2}
    ----
    ----

        L[ (3, 2) ]   => 

    {('111', '211'): 3}
    ----
    ----

    It is not printing L[2,3], feel free to try.
