def run():

    a, n = (list(map(int, input().split())))

    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    print(sum(prime[a:]))


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):
        run()
