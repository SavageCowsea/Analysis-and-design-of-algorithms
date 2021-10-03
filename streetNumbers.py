import numpy as np


def run():
    try:
        houses = int(input(' Enter a positive integer '))
        if houses < 3:
            print(-1)
        else:
            #neighborhood = [i for i in range(1, houses)]
            neighborhood = np.arange(houses)
            print(neighborhood[0:houses:2])

    except TypeError:
        print(' Error!')


if __name__ == '__main__':
    run()
