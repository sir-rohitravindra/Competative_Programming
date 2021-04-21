import math
for t in range(int(input())):
    h,x,y,c=(int(i) for i in input().split())

    if (x+math.floor(y/2))*h>c:
        print("NO")
    else:
        print("YES")