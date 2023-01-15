#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    if b.find("_") >= 0:
        b = ''.join(sorted(b))
    b = "_" + b + "_"
    for i in range(1,len(b)-1):
        if b[i] != "_":
            if b[i] != b[i-1] and b[i] != b[i+1]:
                return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()

items = [0]
for i in range(int(input())):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        items.append(max(nums[1], items[-1]))
    elif nums[0] == 2:
        items.pop()
    else:
        print(items[-1])