#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(s1, s2, s3):
    h1 = sum(s1)
    h2 = sum(s2)
    h3 = sum(s3)
    minh = min(h1, h2, h3)
    while minh > 0:
        while h1 > minh:
            h1 = h1 - s1.pop(0)
        while h2 > minh:
            h2 = h2 - s2.pop(0)
        while h3 > minh:
            h3 = h3 - s3.pop(0)
        if h1 == h2 and h2 == h3:
            break
        minh = min(h1, h2, h3)
    return minh

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
