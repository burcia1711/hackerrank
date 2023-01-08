#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    M = 1000000007

    a = [0, 1, 2, 4, 8]
    for j in range(5, m + 1):
        a.append((a[j - 1] + a[j - 2] + a[j - 3] + a[j - 4]) % M)

    for i in range(m + 1):
        a[i] = pow(a[i], n, M)

    r = [a[i] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, i):
            r[i] -= (r[j] * a[i - j])
        r[i] = r[i] % M
    return r[m]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
