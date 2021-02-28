for i in range(int(input())):
    (d,c)=[int(i) for i in input().split()]
    n1=sum([int(i) for i in input().split()])<150
    pays=(2-n1-(sum([int(i) for i in input().split()])<150))*d
    if(pays+c<(2*d)):
        print("YES")
    else:
        print("NO")
