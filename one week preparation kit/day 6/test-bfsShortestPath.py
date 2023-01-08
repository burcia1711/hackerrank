#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    queue = [s]
    visited = [s]
    dists = {s: 0}
    adjList = {}
    for i in range(len(edges)):
        edge = edges[i]
        x = edge[0]
        y = edge[1]
        if x in adjList:
            if y not in adjList[x]:
                adjList[x].append(y)
        else:
            adjList[x] = [y]
        if y in adjList:
            if x not in adjList[y]:
                adjList[y].append(x)
        else:
            adjList[y] = [x]
    while len(queue) > 0:
        node = queue.pop(0)
        if node in adjList:
            neighbors = adjList[node]
            for j in range(len(neighbors)):
                if neighbors[j] not in visited:
                    dists[neighbors[j]] = dists[node] + 6
                    visited.append(neighbors[j])
                    queue.append(neighbors[j])
    res = []
    for i in range(1,n+1):
        if i not in dists:
            res.append(-1)
        elif dists[i] != 0:
            res.append(dists[i])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
