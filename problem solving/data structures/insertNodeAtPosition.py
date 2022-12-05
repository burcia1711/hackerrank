#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    res = False
    i = 1
    if v2 > v1:
        if x2 > x1:
            return "NO"
    else:
        for i in range(10000):
            f_pos = x1 + (i * v1)
            s_pos = x2 + (i * v2)
            if (f_pos == s_pos):
                return "YES"
                res = True
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
