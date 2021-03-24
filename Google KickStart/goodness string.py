for t in range(int(input())):

    n,k=(int(i) for i in input().split())
    #print("####",n,k)
    str=input()

    goodness=0

    for i in range(len(str)//2):
        #print("#",str[i],i)
        if not(str[i]==str[-i-1]):
            goodness+=1

    print("Case #{}: {}".format(t+1,abs(goodness-k)))