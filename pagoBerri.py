

def amount(value: int) -> int:
    count: int = 0
    MONEY = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
    index = 0
    v = 0
    while(count != value):
        if(MONEY[index] <= value and MONEY[index]+count <= value):
            count += MONEY[index]
            v += 1
        else:
            index += 1
    return v


def run():
    number = int(input())
    print(amount(number))


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):
        run()
