for t in range(int(input())):
    s=int(input())
    cs=0
    q=[int(i) for i in input().split()]
    time=sum(q)
    for _ in range(s):
        time+=sum([int(i)-q[cs] for i in input().split()[1:]])
        cs+=1
    print(time)