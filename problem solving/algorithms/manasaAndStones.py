#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    valid = True

    counts = dict()
    for i in s:
        counts[i] = counts.get(i, 0) + 1

    items = list(counts.values())
    print(items)

    if max(items) - min(items) == 0:
        return "YES"

    if items.count(max(items)) == 1:
        if max(items) - min(items) == 1 or max(items) - min(items) == 0:
            return "YES"
        else:
            return "NO"

    if items.count(max(items)) > 1:
        if items.count(min(items)) == 1 and min(items) == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
