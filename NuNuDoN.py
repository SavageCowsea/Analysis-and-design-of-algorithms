import math


def printDivisors(n):

    i = 1
    count = 0
    while i <= math.sqrt(n):

        if (n % i == 0):

            if (n / i == i):
                # print(i)
                count += 1
            else:

                #print(i, n/i,)
                count += 2
        i = i + 1
    return(count)


def run():
    a, b = ((list(map(int, input().split()))))
    init = 1
    count = 0

    while(init <= b):
        if(init >= a):
            # print(init)
            count += 1
            init = printDivisors(init)+init
        else:
            init = printDivisors(init)+init
    print(count)


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):

        run()
