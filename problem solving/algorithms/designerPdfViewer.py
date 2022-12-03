#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    listx=list(range(1,len(p)+1))
    result=[]
    ans_arr=[]
    for j in listx:
        for i in range(len(p)):
            if j==p[i]:
                result.append(i+1)
    for i in result:
        for j in range(len(p)):
            if i==p[j]:
                ans_arr.append(j+1)
    return ans_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
