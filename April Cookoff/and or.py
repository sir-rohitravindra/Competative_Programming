from functools import reduce
for t in range(int(input())):

    n,q=(int(i) for i in input().split())
    ar=[int(i) for i in input().split()]
    print(reduce(lambda a, b: a|b, ar))
    for qr in range(q):
        x,v=[int(i) for i in input().split()]
        ar[x-1]=v
        print(reduce(lambda a, b: a | b, ar))



