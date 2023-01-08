if __name__ == '__main__':
    s = ''
    stack = []
    q = int(input())
    for t in range(q):
        op = input().split()
        if op[0] == '1':
            stack.append(s)
            s += op[1]
        if op[0] == '2':
            stack.append(s)
            _len = len(s) - int(op[1])
            s = s[:_len]
        if op[0] == '3':
            no = int(op[1]) - 1
            print(s[no])
        if op[0] == '4':
            s = stack.pop()