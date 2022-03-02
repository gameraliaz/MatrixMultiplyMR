#!/usr/bin/env python
"""mapper.py"""

# Mapper for Matrix A (k, v)=((i, k), (A, j, Aij)) for all k
# Mapper for Matrix B (k, v)=((i, k), (B, j, Bjk)) for all i

import sys

A=open("cache_inp").readlines()
firstMat=A[0].split('(')[0]

# A(2,2)
# B(2,2)

firstMatRow, secondMatCol = map(int,[A[0].split('(')[1].split(",")[0],A[1].split(',')[1].replace(')','')])

for line in sys.stdin:
    
    matrixName, row, col, value = line.rstrip().split(",")

    if matrixName==firstMat:
        for i in range(1,secondMatCol+1):
            key = row + "," + str(i)
            print(f"(({key}),{matrixName},{col},{value})")
    else:
        for j in range(1,firstMatRow+1):
            key = str(j) + "," + col
            print(f"(({key}),{matrixName},{row},{value})")