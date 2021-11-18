def suma(arr):
    if arr[3] == 'I':
        return 20
    else:
        return int(arr[2])


def scorecalculator(d: dict):
    for i in d.keys():
        if i == 'I':
            d[i]
    pass


def run():
    m = int(input())
    for i in range(m):
        r = int(input())
        arr = [list(map(str, input().split())) for x in range(r)]
        o = filter(lambda x: x[3] != 'R' and x[3] != 'U' and x[3] != 'E', arr)
        #y = o
        # print(list(y))
        ans = {}
        inval = {}
        eligible = {}
        debt = {}
        for j in o:
            if j[0] not in ans:

                if j[3] == 'C':
                    ans[j[0]] = [0, suma(j)]
                    inval[j[0]+j[1]] = True
                    eligible[j[0]] = True
                    ans[j[0]][0] += 1
                    if j[0]+j[1] in debt:
                        ans[j[0]][1] += debt[j[0]+j[1]]
                        del debt[j[0]+j[1]]
                else:
                    if j[0]+j[1] not in inval:
                        if j[0]+j[1] not in debt:
                            debt[j[0]+j[1]] = suma(j)
                        else:
                            debt[j[0]+j[1]] += suma(j)
            elif (j[0] in ans and j[0]+j[1] not in inval):

                if j[3] == 'C':
                    ans[j[0]][1] += suma(j)
                    ans[j[0]][0] += 1
                    inval[j[0]+j[1]] = True
                    eligible[j[0]] = True
                    if j[0]+j[1] in debt:
                        ans[j[0]][1] += debt[j[0]+j[1]]
                        del debt[j[0]+j[1]]
                else:
                    if j[0]+j[1] not in inval:
                        if j[0]+j[1] not in debt:
                            debt[j[0]+j[1]] = suma(j)
                        else:
                            debt[j[0]+j[1]] += suma(j)

        ans = dict(sorted(ans.items(), key=lambda item: [
                   item[1][0], -item[1][1], -int(item[0])], reverse=1))
        # print(inval)
        print('maraton', f'{i+1}:')
        for key, values in ans.items():
            if(key in eligible):
                print(key, *values)

        #print(inval, eligible)
        ans = {}
        inval = {}
        eligible = {}
        if(i < m-1):
            print()
        # *sorted(ans.items(), key=lambda item: item[1], reverse=1)


if __name__ == '__main__':
    run()
