#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    ratios = [0, 0, 0]
    n = len(arr)
    for i in arr:
        if i > 0:
            ratios[0] += 1
        elif i < 0:
            ratios[1] += 1
        else:
            ratios[2] += 1

    print("{:.6f}".format(ratios[0] / n))
    print("{:.6f}".format(ratios[1] / n))
    print("{:.6f}".format(ratios[2] / n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
