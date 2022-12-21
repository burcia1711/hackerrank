def n_length_combo(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]

        remainlst_combo = n_length_combo(remLst, n - 1)
        for p in remainlst_combo:
            l.append([m, *p])

    return l

print(n_length_combo([1,2,3,4,5],3))