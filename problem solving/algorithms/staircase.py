#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minMax = [0, 0]
    sum = 0
    n = len(arr) - 1
    for i in arr:
        sum += i
    minMax[0] = sum - arr[n]
    minMax[1] = sum - arr[0]

    print('{} {}'.format(minMax[0], minMax[1]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
