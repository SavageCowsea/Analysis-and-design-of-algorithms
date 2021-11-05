import math
from functools import reduce


arr = [1 for i in range(0, 1000000)]

s = 2

for i in range(s, len(arr)+1, s):
    for j in range(s, len(arr)+1, s):
        arr[j-1] += 1
    s += 1

iter = int(input())

for _ in range(iter):
    num = int(input())
    print(arr[num-1])
