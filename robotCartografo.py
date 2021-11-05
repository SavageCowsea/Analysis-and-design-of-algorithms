from itertools import count, product, combinations_with_replacement


""" def check(possible, ad: list) -> bool:
    melo = True
    for i, ii in enumerate(possible):
        for j, ji in enumerate(ad[i]):
            if(i != j and ii == possible[j] and ji == 1):
                melo = False
                return melo
    return melo """


def check(possible, ad: list) -> bool:
    melo = True
    for i, ii in enumerate(ad):
        for j, ji in enumerate(ii):
            k = possible[i]
            q = possible[j]
            if(i != j and k == q and ji == 1):
                melo = False
                return melo
    return melo


def f(l: list, s: int, n: int, c: list) -> int:
    count = n
    if s == n:
        yield l
    else:
        for i in range(s+1):
            l[s] = i
            yield from f(l, s+1, n, c)


def run():
    # sentinel = ''
    # print(list('\n'.join(iter(input, sentinel)).replace('\n',)))
    a_matrix = []
    colors = int(input())
    colors1 = colors
    gh = colors
    ful = False
    for rows in range(colors):
        addd = list(map(int, input().split()))
        a_matrix.append(addd)
        if 0 in addd:
            colors = gh
    if gh != colors:
        ful = True

        # print(a_matrix)
    o = colors

    #a = combinations_with_replacement([i for i in range(colors)], colors)

    if(ful == True):
        print(colors)

    else:
        a = f([0]*colors1, 0, o, a_matrix)
        while(True):

            try:
                b = next(a)

                # print(list(b))
                if (check(b, a_matrix) == True):
                    # print(list(b))
                    print(len(set(b)))
                    break
            except StopIteration:
                break
                #a = f([0]*colors, 0, o, a_matrix)


if __name__ == '__main__':
    x = int(input())
    for _ in range(x):
        run()
