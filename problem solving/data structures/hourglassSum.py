#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    lastAnswer = 0
    ans = []
    arr = [[] for i in range(n)]

    for query in queries:
        check = query[0]
        x = query[1]
        y = query[2]
        idx = (x ^ lastAnswer) % n
        # idx = ((x and not lastAnswer) or (not x and lastAnswer)) % n
        if check == 1:
            arr[idx].append(y)
        elif check == 2:
            if (len(arr[idx]) == 0):
                print(arr[idx])
            lastAnswer = arr[idx][y % len(arr[idx])]
            ans.append(lastAnswer)

    print(ans)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
