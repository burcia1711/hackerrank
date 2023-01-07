s1 = []
s2 = []


def enqueue(num):
    s1.append(num)


def dequeue():
    if s2:
        s2.pop()
    elif s1:
        while s1:
            s2.append(s1.pop())
        s2.pop()
    else:
        return


def printqueue():
    if s2:
        print(s2[-1])
    elif s1:
        print(s1[0])
    else:
        print("Empty")


for _ in range(int(input())):
    query = input()
    if " " in query:
        if query.split()[0] == "1":
            enqueue(query.split()[1])
    else:
        if query == "2":
            dequeue()
        if query == "3":
            printqueue()