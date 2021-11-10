source = input().split("/")
destination = input().split("/")
min_lenght = min(len(source),len(destination))

A=[]
D=[]

review_sufix = True
review_prefix = True
for i in range(min_lenght):
    if source[i] == destination[i] and review_prefix:
        A.append(source[i])
    else:
        review_prefix = False

    if source[(i+1)*-1] == destination[(i+1)*-1] and review_sufix:
        D = [source[(i+1)*-1]] + D
    else:
        review_sufix = False

    if not review_prefix and not review_sufix:
        break

B = source[len(A):len(source)-len(D)]
C = destination[len(A):len(destination)-len(D)]

B = "/".join(B)
C = "/".join(C)

if len(A) > 0:
    A = "/".join(A) + "/"
else:
    A = ""
        
if len(D) > 0:
    D= "/" + "/".join(D)
else:
    D = ""
    
output = str(A) + "{" + str(B) + " => " + str(C) + "}"+ str(D)
print(output)