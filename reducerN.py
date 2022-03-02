#!/usr/bin/env python
"""reducer.py"""

# Reducer(k, v)=(i, k)=>Make sorted Alist and Blist
# (i, k) => Summation (Aij * Bjk)) for j
# Output =>((i, k), sum)


import sys
from operator import itemgetter

prevKey = None
value_list = []

for line in sys.stdin: # ((2,1),A,1,3)
    Line=line.rstrip().replace('(','').replace(')','').split(',') # [2,2,A,1,3]
    currKey = Line[0]+','+Line[1] # '2,2'
    index,value = map(int,[Line[3],Line[4]]) # int 1 , int 3

    if currKey == prevKey:
        value_list.append((index,value))
    else:
        if prevKey:
            value_list = sorted(value_list,key=itemgetter(0))
            i = 0
            result = 0
            while i < len(value_list) - 1:
                if value_list[i][0] == value_list[i + 1][0]:
                    result += value_list[i][1]*value_list[i + 1][1]
                    i += 2
                else:
                    i+=1
            print(f"{prevKey},{str(result)}")
        prevKey = currKey
        value_list = [(index,value)]

if currKey == prevKey:
    value_list = sorted(value_list,key=itemgetter(0))
    i = 0
    result = 0
    while i < len(value_list) - 1:
        if value_list[i][0] == value_list[i + 1][0]:
            result += value_list[i][1]*value_list[i + 1][1]
            i += 2
        else:
            i+=1
    print(f"{prevKey},{str(result)}")



