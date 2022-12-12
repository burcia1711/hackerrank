def median(arr1, arr2):
    sum = 0
    count = 0
    for i in range(len(arr1)):
        sum+=arr1[i]
        count+=1
    for i in range(len(arr2)):
        sum+=arr2[i]
        count+=1
    return (sum/count)

res = median([1,2,3],[1,2])
print(res)