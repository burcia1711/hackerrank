#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#


def kaprekarNumbers(p, q):
    lst = []
    for i in range(p, q+1):
        sq = i**2
        d = len(str(i))
        r = str(sq)[-d:]
        l = str(sq)[:-d]
        if l == '':
            l = 0
        if int(l) + int(r) == i:
            lst.append(i)
    if len(lst) == 0:
        print('INVALID RANGE')
    else:
        print(*lst)


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
