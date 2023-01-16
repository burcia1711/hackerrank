import heapq

Q = input()
heap = []
delset = set()
for _ in range(int(Q)):
    q = input()
    if len(q) == 1:
        while heap[0] in delset:
            heapq.heappop(heap)
        print(heap[0])
    else:
        n1 = int(q[0])
        n2 = int(q[2:])
        if n1 == 1:
            heapq.heappush(heap, n2)
        else:
            delset.add(n2)