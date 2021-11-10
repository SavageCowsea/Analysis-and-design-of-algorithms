from bisect import insort


def run():
    number = int(input())
    arr = []
    for _ in range(number):
        arr.append(int(input()))
    arr = sorted(arr)
    count = 0
    while(len(arr) >= 2):
        if(arr[0]+arr[-1] >= 1000):
            count += 1
            arr.pop(0)
            arr.pop(-1)

        else:
            arr.pop(0)

    print(count)


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):
        run()
