#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c = sorted(c)
    maxDistance = max (c[0], n - c[-1] - 1)
    last_city = c[0]
    for i in range(1, len(c)):
        distance = (c[i] - last_city) // 2
        maxDistance = max(maxDistance, distance)
        last_city = c[i]
    return maxDistance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
