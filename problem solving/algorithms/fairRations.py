#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    loaves = 0
    for i in range(1, len(B)):
        if B[i-1] % 2 == 1:
            B[i] += 1
            loaves += 2
    if B[-1] % 2 == 0:
        return str(loaves)
    else:
        return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
