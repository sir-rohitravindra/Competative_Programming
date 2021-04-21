for t in range(int(input())):

    n,m=(int(i) for i in input().split())

    tl={int(i) for i in input().split()}
    #print("   * ",type(tl))
    if(len(tl)<m):
        print("Yes")
    else:
        print("No")