#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    max_length = 0
    possible_solutions = {i: list() for i in range(0, 101)}

    for i in a:
        possible_solutions[i].append(i)
        if len(possible_solutions[i]) > max_length:
            max_length = len(possible_solutions[i])

        possible_solutions[i + 1].append(i)
        if len(possible_solutions[i + 1]) > max_length:
            max_length = len(possible_solutions[i + 1])

    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
