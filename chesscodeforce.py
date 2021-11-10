w = {'Q': 9, 'K': 0, 'P': 1, 'R': 5, 'B': 3, 'N': 3,
     'q': 9, 'k': 0, 'p': 1, 'r': 5, 'b': 3, 'n': 3, '.': 0}
bp = 0
wp = 0
for _ in range(8):
    i = input().split('\n')
    for j in i[0]:
        if(j == 'Q' or j == 'K' or j == 'B' or j == 'N' or j == 'P' or j == 'R'):
            wp += w[j]
        else:
            bp += w[j]

if (wp > bp):
    print('White')

elif(bp > wp):
    print('Black')

else:
    print('Draw')
