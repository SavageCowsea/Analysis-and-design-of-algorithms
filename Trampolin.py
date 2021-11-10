def run():
    number: int = int(input())
    # arr = {}
    arr = [list(map(int, input().split())) for i in range(number)]
    # arr = {i: list(map(int, input().split())) for i in range(number)}
    # arr = dict(sorted(arr.items(), key=lambda x: x[1][1], reverse=1))
    arr = list(sorted(arr, key=lambda x: x[1], reverse=1))
    arr1 = [0 for i in range(number)]
    tantrum = 0
    for i, j in enumerate(arr):
        aux = False
        if(arr1[int(j[0]/10)] == 0):
            arr1[int(j[0]/10)] = j
            aux = True
        else:
            n = (int(j[0]/10))-1
            while(n >= 0):
                if(arr1[n] == 0):
                    arr1[n] = j
                    aux = True
                    break
                n -= 1
        if aux == False:
            arr1.insert(number-1, j)
            tantrum += j[1]

    print(tantrum)


if __name__ == '__main__':
    iter = int(input())
    for i in range(iter):
        run()
