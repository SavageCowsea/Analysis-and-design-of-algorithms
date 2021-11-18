from itertools import product


def run():
    N = list(map(int, input().split()))
    arr = []
    for _ in range(N[0]):
        arr.append(int(input()))
    arr = sorted(arr)
    #a = (product(arr, repeat=2))
    base = N[0]**2
    ans = 1
    for p in range(1, N[0]+1):
        if(N[0]*p >= N[1]):
            ans = p
            g = N[1] % N[0]
            break

    print(arr[p-1], arr[g-1])
    """ for l in range(N[1]):
        print(next(a)) """
    """ for l in a:
        print(l) """

    #print(*sorted(product(arr, repeat=2), key=lambda x: [x[0], x[1]])[N[1]-1])


if __name__ == '__main__':
    run()
