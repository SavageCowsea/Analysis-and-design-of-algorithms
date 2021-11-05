import itertools
from functools import reduce


def combination(arr, time, n, no):
    all_combinations = itertools.combinations(arr, n)
    all_combinations = list(filter(lambda x: sum(x) <= time, all_combinations))
    if (len(all_combinations) != 0):
        return time-sum(reduce(lambda a, b: a if time-sum(a) <= time -
                               sum(b) else b, all_combinations))
    else:
        return no


def awaitingtime(songs, time):
    ans = -1
    if len(songs) == 0:
        return time
    elif sum(songs) == time or time in songs:
        return 0
    elif sum(songs) < time:
        return time-sum(songs)
    elif sum(songs) > time:
        n = 1
        while(ans != 0 and n <= len(songs)):
            ans = combination(songs, time, n, ans)
            n += 1
        return ans


def run():
    a = list(map(int, input().split()))
    time = a[0]
    a.pop(0)
    a = list(filter(lambda x: x <= time, a))
    print((awaitingtime(a, time)))


if __name__ == '__main__':
    iter = int(input())

    for _ in range(iter):

        run()
