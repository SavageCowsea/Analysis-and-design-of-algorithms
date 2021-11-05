from itertools import combinations


def run():
    f: int = int(input())
    arr: list = []
    for _ in range(f):
        arr.append(list(map(str, input().split())))
    # print(arr)

    minutes = all_minutes(arr)
    ok_times = ok_time(minutes)
    #print(minutes, '\n', ok_times)

    # print(not_overlap([800, 928], [929, 1100]))
    print(last_selection(minutes, ok_times))


def hours_to_min(times: str) -> int:
    ftr = [60, 1]
    if(times == '00:00'):
        minutes = 24*60

    else:
        minutes = sum([a*b for a, b in zip(ftr, map(int, times.split(':')))])

    return (minutes)


def days_to_min(days: str) -> int:
    dic = {'sabado': 0, 'domingo': 1440, 'lunes': 2880}
    return dic.get(days)


def all_minutes(arr: list) -> list:
    minutes = []
    for i in arr:
        minutes.append([days_to_min(i[0]) + hours_to_min(i[1]), days_to_min(i[0]) + hours_to_min(i[1]) +
                        int(i[2])])
    return minutes


def ok_time(arr: list) -> list:
    arr1 = []
    # print(arr)
    for j, i in enumerate(arr):
        # print(i[0], i[1])
        if 360 <= i[0] <= 1440:
            if 360 <= i[1] <= 1440:
                arr1.append(j)

        elif 1800 <= i[0] <= 2880:
            if 1800 <= i[1] <= 2880:
                arr1.append(j)

        elif 3240 <= i[0] <= 4320:
            if 3240 <= i[1] <= 4320:
                arr1.append(j)

    return arr1


def not_overlap(fam1: list, fam2: list) -> bool:
    # not(fam1[0] <= fam2[0] <= fam1[1]) and not(fam1[0] <= fam2[1] <= fam1[1])
    arr = [fam1, fam2]
    arr = sorted(arr, key=lambda x: x[1])
    if(arr[0][1] <= arr[1][0]):
        return True
    else:
        return False


def Overlap(arr: list):
    arr2 = list(arr)
    for i, v in enumerate(arr2):
        copia = arr2.copy()
        del copia[i]
        # print(len(arr2))
        # print(len(copia))
        for y in copia:
            if(not_overlap(v, y) == False):
                return False
    return True


def last_selection(fam: list, fam1: list) -> int:
    arr_r = []
    if(len(fam1) == 0):
        return 0
    for i in fam1:
        arr_r.append(fam[i])

    # print(arr_r)
    for i in range(len(fam), 0, -1):
        d = combinations(arr_r, i)
        for j in d:
            if Overlap(j) == True:
                return i
    return 1


if __name__ == '__main__':
    iter = int(input())
    for _ in range(iter):
        run()
