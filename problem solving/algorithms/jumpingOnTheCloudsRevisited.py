import os


def jumpingOnClouds(C, K):
    e = 100
    N = len(C)
    i = 0
    while i <= N:
        if C[(i+K) % N] == 1:
            e -= 3
        else:
            e -= 1
        if (i+K) % N == 0:
            break
        i += K
        if i > N:
            i = i % N
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
