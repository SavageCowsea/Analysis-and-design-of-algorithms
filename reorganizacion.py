from math import ceil, floor


def printlietr(arr):
    print(*arr, sep='')


def mergeSort(X):
    M = len(X)
    if M > 1:
        XL = (X[:floor(M/2)]).copy()
        XR = (X[floor(M/2):]).copy()
        #printlietr(merge(mergeSort(XL), mergeSort(XR), M))
        return merge(mergeSort(XL), mergeSort(XR), M)
    else:
        printlietr(X)
        return X

    # print('\n')


def merge(XL, XR, M):
    i, j, k = 0, 0, 0
    Zk = []
    while(k < M):

        if(i >= floor(M/2)):
            # print(Zk)
            Zk.append(XR[j])
            j += 1

        elif(j >= M-floor(M/2)):
            Zk.append(XL[i])
            i += 1

        elif(XL[i] <= XR[j]):
            Zk.append(XL[i])
            i += 1

        elif(XL[i] > XR[j]):
            Zk.append(XR[j])
            j += 1

        k += 1

    printlietr(Zk)
    return Zk


def run(i, iter):
    num = list(map(int, input().split()))
    print(f'caso {i+1}:')
    mergeSort(num)
    if(i < iter-1):
        print()


if __name__ == '__main__':
    iter = int(input())
    for i in range(iter):
        run(i, iter)
