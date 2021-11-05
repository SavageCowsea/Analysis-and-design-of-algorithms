from math import ceil, floor, gcd, sqrt
from math import ceil, floor, gcd


def run():

    a = int(input())
    for i in range(a):
        arr = [i for i in list(range(2, ceil((a+1)/2))) if a % i == 0]

    print(len(arr)+2)


def run():

    b = int(input())
    for i in range(b):
        a = int(input())
        arr = [i for i in list(range(2, ceil(sqrt((a+1)/2)))) if a % i == 0]

        print(len(arr)+2)


if __name__ == '__main__':
    run()

if __name__ == '__main__':
    run()
