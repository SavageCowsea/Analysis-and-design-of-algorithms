import itertools


def trimuda(arr, val):
    if(sum(arr[:4]) == val and sum(arr[3:7]) == val and sum(arr[6:9]+arr[0:1]) == val):
        return True
    else:
        return False


def run():
    a = ((list(map(int, input().split()))))
    print(
        sum(map(lambda x: trimuda(x, a[0]) == True, (itertools.permutations(a[1:])))))


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):
        run()
