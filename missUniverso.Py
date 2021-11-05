def DO_BOARD(N):
    BOARD = [[0 for i in range(N)] for i in range(N)]
    return BOARD


def CHECK_SOLUTIONS(LEFT_QUEENS, BOARD):
    pass


def run():
    N = list(map(int, input().split()))
    P = N[1:]
    N = N[0]
    LEFT_QUEENS = N-2
    BOARD = DO_BOARD(N)
    BOARD[P[0]-1][P[1]-1] = 1
    BOARD[P[2]-1][P[3]-1] = 1
    print(BOARD)


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):
        run()
