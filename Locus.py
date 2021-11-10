def lcm(a, b):  # algoritmo de Euclides
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1

    return lcm


k = int(input())
a = []
for i in range(k):
    L = list(map(int, input().split()))
    X = lcm(L[1], L[2])
    a.append(L[0]+X)
print(min(a))
