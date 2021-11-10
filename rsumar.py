from sys import stdin, stdout
from functools import reduce
from itertools import permutations
from math import ceil, floor
from bisect import insort


def newsum(arr: list, number):
    #print(sup, inf)
    sum = 0
    w = 0
    #print('suma:********', suma)
    while(len(arr) != 1):
        a = arr.pop(0)
        b = arr.pop(0)
        c = a+b
        w += c
        insort(arr, c)
    stdout.write(str(w)+'\n')


def run():
    while(True):
        number: int = int(stdin.readline())

        if(number == 0):
            break
        arr = ([int(stdin.readline().strip())
                for i in range(number)])
        """ for k in permutations(arr):
            newsum(k, number) """
        newsum(sorted(arr), number)
        #newsum(arr[3:4], number)


if __name__ == '__main__':
    run()
