arr1 = list(map(int, input().split()))
arr2 = sorted(list(map(int, input().split())))
arr3 = arr2.copy()
min = 0
max = 0

w = arr1[1]-1
for i in range(arr1[0]):
    if(arr2[w] >= arr2[w-1]):
        max += arr2[w]
        arr2[w] -= 1

    else:
        max += arr2[w-1]
        arr2[w-1] -= 1
        w -= 1


t = 0
n = arr1[0]
while(n != 0):
    if arr3[t] != 0:
        min += arr3[t]
        arr3[t] -= 1
        n -= 1
    else:
        t += 1


print(max)
print(min)
