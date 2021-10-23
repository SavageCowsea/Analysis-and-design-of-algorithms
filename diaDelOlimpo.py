#from functools import reduce
from math import lcm, gcd


""""def gcd(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b"""


"""def lcm(numbers):
    return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)"""


def run():
    n = int(input())
    for i in range(n):
        a = (list(map(int, input().split())))
    lcm = 1
    for i in a:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)


if __name__ == '__main__':
    run()
