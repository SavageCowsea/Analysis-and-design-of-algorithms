def run(c):
    letters = int(input())
    arr = {}
    for _ in range(letters):
        A, B = input().split()
        """ print(A)
        print(B) """
        arr[A] = int(B)
    freq = (dict(sorted(arr.items(), key=lambda item: item[1])))
    a_view = freq.items()
    freq = list(a_view)
    print(freq)


if __name__ == '__main__':
    iter = int(input())
    for i in range(iter):
        run(i)
