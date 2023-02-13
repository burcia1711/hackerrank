A = set(input().split())
counter = 0
N = int(input())
for i in range(N):
        B = set(input().split())
        if A.issuperset(B):
            counter += 1
print(counter == N)