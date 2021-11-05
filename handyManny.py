from functools import reduce
iter = int(input())


def product(arr: list) -> list:
    b = []
    for i, w in enumerate(arr):
        b.append([reduce(lambda x, y: y/x, w), w[0], w[1]])
    yield b


def finned(arr: list) -> int:
    time = 0
    total = sum(x[1] for x in arr)
    multa = 0
    i = 0
    while(time != total):
        time += arr[i][1]
        multa += (time-arr[i][1])*arr[i][2]
        i += 1
    return multa


for _ in range(iter):
    works = int(input())
    arr = []
    for _ in range(works):
        arr.append(list(map(int, input().split())))
    produc = sorted(next(product(arr)), key=lambda x: x[0], reverse=1)
    # print(produc)
    print(finned(produc))
