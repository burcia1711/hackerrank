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
    tot = len(arr)
    pos = 0
    neg = 0
    zero = 0

    for i in range(tot):
        if arr[i] == 0:
            zero += 1
        elif arr[i] > 0:
            pos += 1
        else:
            neg += 1
    print(pos / tot)
    print(neg / tot)
    print(zero / tot)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
