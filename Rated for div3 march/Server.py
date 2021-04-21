import math
for i in range(int(input())):

    n,k=(int(i) for i in input().split())

    n1=math.ceil(n/k)
    n2=math.floor(n/k)

    if(n1==n2):
        print(n1,k)
    else:
        l=(n-(k*n2))/(n1-n2)
        print(n1,int(l))