#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    strt = 1
    for i in range(0, n):
        if n == 0:
            strt = 1
        elif i % 2 == 0:
            strt *= 2
        else:
            strt += 1
    return strt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
