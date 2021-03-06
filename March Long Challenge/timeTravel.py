n,h,x=[int(i) for i in input().split()]
dif=h-x

list=[int(i)>=dif for i in input().split()]

if(True in list):
    print("YES")
else:
    print("NO")

