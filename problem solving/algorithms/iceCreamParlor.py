#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    res = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if j != i:
                f_i = arr[i]
                s_i = arr[j]
                if f_i + s_i == m:
                    res.append(i + 1)
                    res.append(j + 1)
        if len(res) == 2:
            break

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
