import os
import re


def hexColorCheck(s):
    w = s.split()
    if len(w) > 1 and '{' not in w:
        w = re.findall(r'#[a-fA-F0-9]{3,6}', s)
        [print(i) for i in w]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())

    for i in range(n):
        s = input()
        hexColorCheck(s)

    fptr.close()



# ----------
# import re
#
# n = int(input())
#
# for i in range(n):
#    s = input()
#
#   w = s.split()
#    if len(w) > 1 and '{' not in w:
#        w = re.findall(r'#[a-fA-F0-9]{3,6}', s)
#        [print(i) for i in w]
