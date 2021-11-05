from itertools import permutations, combinations
from collections import Counter


iter: int = int(input())
for _ in range(iter):
    num_str: str = (input())
    if len(num_str) % 2 != 0:
        print('No')
    else:
        num_int: int = int(num_str)
        mitad: int = int(len(num_str)/2)
        valor = False
        for i in permutations(num_str):
            if(int(''.join((list(i))[:mitad]))*int(''.join((list(i))[mitad:])) == num_int):
                print('Heredero')
                valor = True
                break
        if valor == False:
            print('No')
