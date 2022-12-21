#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#
def workbook(n, k, arr):
    specials = 0
    page = 0
    for chapter in range(n):
        for questions in range(arr[chapter]):
            if questions % k == 0 or (questions + 1) == 1:
                page = page + 1
            if page == questions + 1:
                specials = specials + 1
    return specials


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
