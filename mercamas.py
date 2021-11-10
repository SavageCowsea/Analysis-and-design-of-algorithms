from sys import stdin, stdout


def run():
    articles = int(stdin.readline())
    for _ in range(articles):
        arr = sorted(
            list(map(int, stdin.readline().strip().split())), reverse=1)
        sum = 0
        for i, j in enumerate(arr):
            if (i+1) % 3 == 0:
                sum += j
        stdout.write(str(sum)+'\n')


if __name__ == '__main__':
    run()
