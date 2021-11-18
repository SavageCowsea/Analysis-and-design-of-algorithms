from ast import Index
import bisect


def run():
    N, Q = input().split()
    arr, arr1 = [], []
    for _ in range(int(N)):
        arr.append(int(input()))

    for _ in range(int(Q)):
        arr1.append(int(input()))

    arr = sorted(arr)

    for j in arr1:
        try:
            print(j, 'se encuentra en', arr.index(j)+1)
        except:
            print(j, 'no se encuentra')


if __name__ == '__main__':
    run()
