import os


def viralAdvertising(n):
    summ = 0
    a = 5
    for _ in range(n):
        a = a//2
        summ += a
        a = a*3
    return summ


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
