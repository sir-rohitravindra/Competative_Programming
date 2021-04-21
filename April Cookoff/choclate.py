for t in range(int(input())):

    n,x=[int(i) for i in input().split()]

    a=[int(i) for i in input().split()]
    a.sort()

    count=1
    bro=0
    prev=a[0]
    for i in a[1:]:
        if(i!=prev):
            count+=1

        else:
            bro+=1
        prev = i


    if(bro<x):
        count-=x-bro
    print(count)


