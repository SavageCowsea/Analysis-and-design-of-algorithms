from itertools import product


def yielder(arr):
    ans = -1
    gen = (product({'t', 's'}, repeat=len(arr)))
    while(True):
        ans1 = 0
        try:
            play1 = next(gen)
            last = ''
            for x, y in enumerate(play1):
                if x != 0:

                    if y == 't':
                        ans1 += arr[x]
                        if last == 't':
                            ans1 = ans1-arr[x-1]
                    last = y
                else:
                    if y == 't':
                        ans1 += arr[x]
                    last = y
            if(ans1 > ans):

                ans = ans1
        except:
            break
    yield ans


def run():
    arr = list(map(int, input().split()))
    print((sum(yielder(arr))))


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):
        run()
