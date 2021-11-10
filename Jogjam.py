def dist(a, b, c, d):
    c1 = abs(c-a)
    c2 = abs(d-b)
    return ((c1**2 + c2**2)**(1/2))


L = list(map(int, input().split()))
d1 = dist(L[0], L[1], L[2], L[3])
d2 = dist(L[4], L[5], L[6], L[7])

if (d2 >= d1):
    if(d2 % 1 == 0):
        print(int(d2))
    else:
        print(round(d2, 10))
else:
    if(d1 % 1 == 0):
        print(int(d1))
    else:
        print(round(d1, 10))
