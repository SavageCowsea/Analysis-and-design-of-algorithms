import math


from math import gcd


def run():

    a, b, n = ((list(map(int, input().split()))))
    div = gcd(a, gcd(b, n))
    a = a/div
    b = b/div
    n = n/div
    print(int(a+b+n))


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):
        run()
