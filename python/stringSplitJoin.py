def split_and_join(line):
    words = line.split(" ")
    newLine = "-".join(words)
    return newLine

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)