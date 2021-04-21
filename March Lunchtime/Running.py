"""import math

for t in range(int(input())):
    x, r, m = (int(i) for i in input().split())

    k = math.floor((60 * r - x) / x)
    print("\t",k*x)
    if (x + (2 * k * x) + (2 * ((60 * r) - x - (k * x))) <= 60 * m):
        print("Yes")
    else:
        print("No", x + (2 * k * x) + (2 * ((60 * r) - x - (k * x))))
"""

for t in range(int(input())):

    n=int(input())
    l=[int(i) for i in input().split()]
    c=[0 for i in range(n)]
    flag=False
    for i in range(n):
        flag=True
        for j in range(i+1,n):
            if(l[j]<l[i]):
                flag=True
            elif(l[j]==l[i] and flag):
                flag=False
                c[i]+=1
                c[j]+=1
            else:
                flag=False
    c=[str(i-1) if i!=0 else "0" for i in c]
    print(" ".join(c))
