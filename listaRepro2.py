import itertools
from functools import reduce


def awaitingtime(a, time):
    if len(a) == 0:
        return time
    elif sum(a) == time or time in a:
        return 0
    elif sum(a) < time:
        return time-sum(a)

    ans = []

    for tam in range(1, len(a)+1):
        try:
            b = sum(reduce(lambda x, y: x if time-sum(x) <= time -
                           sum(y) else y, filter(lambda x: sum(x) <= time, itertools.combinations(a, tam))))
            ans.append(b)
        except:
            break

    try:
        return time-max(ans)
    except:
        return 0

    """ while(True):
        try:
            print(next(a))
        except StopIteration:
            break """


def run():
    a = list(map(int, input().split()))
    time = a[0]
    a.pop(0)
    a = list(filter(lambda x: x <= time, a))
    # print(a)
    print((awaitingtime(a, time)))


if __name__ == '__main__':
    iter = int(input())

    for _ in range(iter):

        run()
