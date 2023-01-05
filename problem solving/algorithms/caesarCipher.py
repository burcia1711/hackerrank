#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    cipherText = ""
    for ch in s:
        up = False
        if ch.isalpha():
            if ch.isupper():
                ch=ch.lower()
                up = True
            stayInAlphabet = ord(ch) + k%26
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            if up:
                finalLetter=finalLetter.upper()
            cipherText += finalLetter
        else:
            cipherText += ch

    return cipherText

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
