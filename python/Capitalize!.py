import os


def solve(s):
    s = s.split(' ')
    return ' '.join([j.capitalize() for j in s])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
