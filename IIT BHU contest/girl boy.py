for t in range(int(input())):
    n=int(input())
    b=[int(i) for i in input().split()]
    g=[int(i) for i in input().split()]
    g.sort()
    b.sort()

    big=b[0]+g[-1]
    for i in range(n):
        if(b[i]+g[-i-1]>big):
            big=b[i]+g[-i-1]
    print(big)
