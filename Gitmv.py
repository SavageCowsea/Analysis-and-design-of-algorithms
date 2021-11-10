import sys
s3 = input()
s4 = input()


s3 = s3.split('/')
s4 = s4.split('/')

""" print(s3)
print(s4) """
r = ''
r2 = ''
p1 = 0
p2 = 0
p3 = 0

for i, j in enumerate(s3):
    if(i > len(s4)-1):
        p1 = i
        print('/'.join(s4) + '/' +
              '{'+'/'.join(s3[p1:])+' => '+'}')
        sys.exit()
    if (j == s4[i]):
        r += j+'/'
    else:
        p1 = i
        break
    if(s3 == s4):
        print('/'.join(s3)+'/'+'{'+' => '+'}')
        sys.exit()
    if(i == len(s3)-1 and len(s4) > len(s3)):
        p1 = len(s3)
        print('/'.join(s3)+'/'+'{'+' => '+'/'.join(s4[p1:])+'}')
        sys.exit()


for i, j in enumerate(reversed(s4)):
    if (j == s3[abs(len(s3)-1-i)]):
        r2 += '/'+j
    else:
        """    r2 = r2[:-1] """
        p2 = abs(i-len(s4)-1)
        p3 = abs(i-len(s3)-1)
        break


print(r+'{'+'/'.join(s3[p1:p3-1])+' => '+'/'.join(s4[p1:p2-1])+'}'+r2)
