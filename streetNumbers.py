import numpy as np
from math import ceil, floor
from functools import reduce


def run():
    a = range(18, 90)
    try:
        for i in range(18, 90, 6):
            print('De', i, 'a', i+5, 'años')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    run()
