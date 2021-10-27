def f(l: list, s: int, n: int) -> int:
    if s == n:
        yield l
    else:
        for i in range(1, n):

            l[s] = i
            yield from f(l, s+1, n)


""" print(next(f([0]*4, 0, len([0]*4))))
print(next(f([0]*4, 0, len([0]*4))))
print(next(f([0]*4, 0, len([0]*4))))
print(next(f([0]*4, 0, len([0]*4)))) """

jmm = (f([0]*4, 0, 4))

while(True):

    try:
        print(next(jmm))
    except:
        break
