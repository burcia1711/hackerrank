def missingTwo(list):
    missing = []
    missed = 2
    size = len(list)
    for i in range(1, size+3):
        if missed:
            miss = 1
            for j in range(len(list)):
                if i == list[j]:
                    miss = 0
                    break
            if miss:
                missing.append(i)
                missed -= 1
        else:
            break
    return missing


res = missingTwo([2, 4, 1, 5])
print(res)