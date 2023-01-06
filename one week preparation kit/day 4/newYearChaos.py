#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    count = 0
    newlist = []
    for g in range(0, len(q)):
        newlist.append(g + 1)
    for i in range(0, len(q)):
        if q[i] - i - 1 > 2:
            print("Too chaotic")
            return
    while True:
        for i in range(0, len(q) - 1):
            if q[i] > q[i + 1]:
                count += 1
                q[i], q[i + 1] = q[i + 1], q[i]
        if q == newlist:
            break
    print(int(count))


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
