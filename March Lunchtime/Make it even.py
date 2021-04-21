for i in range(int(input())):
    input()
    l = [int(i) for i in input().split()]
    ts = l.count(2)
    s = sum(l) % 2
    if s == 0:
        print(0)
    elif (ts>0):
        print(1)
    else:
        print(-1)
