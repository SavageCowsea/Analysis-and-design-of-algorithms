def check(possible, ad: list) -> bool:
    melo = True
    for i, ii in enumerate(possible):
        for j, ji in enumerate(ad[i]):
            if(i != j and ii == possible[j] and ji == 1):
                melo = False
                return melo
    return melo


def f(l: list, s: int, n: int) -> int:
    if s == n:
        yield l
    else:
        for i in range(n):
            l[s] = i
            yield from f(l, s+1, n)


def run():
    # sentinel = ''
    # print(list('\n'.join(iter(input, sentinel)).replace('\n',)))
    a_matrix = []
    colors = int(input())
    for rows in range(colors):
        a_matrix.append(list(map(int, input().split())))

    # print(a_matrix)
    o = 1
    a = f([0]*colors, 0, o)
    while(True):

        try:
            b = next(a)
            print(b)
            if (check(b, a_matrix) == True):

                print(len(set(b)))
                break
        except StopIteration:
            o += 1
            a = f([0]*colors, 0, o)


if __name__ == '__main__':
    x = int(input())
    for _ in range(x):
        run()
