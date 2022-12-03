#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    sticks_cut = []

    while max(arr) > 0:
        cutted_sticks = 0
        min = max(arr)
        for e in arr:
            if e > 0 and e < min:
                min = e
        for i in range(len(arr)):
            if arr[i] > 0:
                cutted_sticks += 1
            arr[i] -= min
        sticks_cut.append(cutted_sticks)

    return sticks_cut


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
