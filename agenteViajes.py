import itertools
from typing import Counter


def run():
    values = []
    cities = int(input())
    routes = list(range(cities))
    solutions = ((itertools.permutations(routes, cities)))
    # (next(solutions))
    for _ in range(cities):
        a = input().split()
        values.append(a)
    # print(values)
    price = 1000000000
    while(True):
        try:

            price1 = 0
            checker = (next(solutions))

            for i in range(cities-1):
                if(values[checker[i]][checker[i+1]] != 'n.a'):
                    price1 += int(values[checker[i]][checker[i+1]])
                else:
                    price1 = price
                    break
            if (price1 <= price):
                price = price1

        except StopIteration:
            if price != 1000000000:
                print(round(price/10, 1))
            else:
                print('imposible')
            break


if __name__ == '__main__':
    iter = int(input())

    for _ in range(iter):

        run()
