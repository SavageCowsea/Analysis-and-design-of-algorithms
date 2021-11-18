import bisect


def run():
    arr = list(map(int, input().split()))
    A: list = []
    B: list = []
    for _ in range(arr[0]):
        A.append(int(input()))

    A = sorted(A)

    for _ in range(arr[1]):
        B.append(int(input()))

    for k in B:
        # print(A)
        if (bisect.bisect_left(A, k)) == 0:
            print('la pareja mas cercana mide', A[0])
        elif (bisect.bisect_left(A, k)) == arr[0]:
            print('la pareja mas cercana mide', A[arr[0]-1])
        else:
            if A[(bisect.bisect_left(A, k))] == k or A[(bisect.bisect_left(A, k))-1] == k:
                print('hay por lo menos una pareja perfecta')

            elif (abs(A[(bisect.bisect_left(A, k))]-k) == abs(A[(bisect.bisect_left(A, k))-1]-k)):
                print('las parejas mas cercanas miden',
                      A[(bisect.bisect_left(A, k))-1], 'y', A[(bisect.bisect_left(A, k))])

            else:
                v = A[(bisect.bisect_left(A, k))-1] if abs(A[(bisect.bisect_left(A, k))]-k) > abs(
                    A[(bisect.bisect_left(A, k))-1]-k) else A[(bisect.bisect_left(A, k))]
                print('la pareja mas cercana mide', v)


if __name__ == '__main__':
    run()
