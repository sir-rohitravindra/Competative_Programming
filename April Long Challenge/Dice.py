for t in range(int(input())):
    n=int(input())

    lst=[0,20,36,51,60]
    if(n<5):
        print(lst[n])
    else:
        lvls=n//4
        lvlsum=lvls*(44)
        tops=n%4
        topsum=(4-tops)*4
        print(lvlsum+topsum+lst[tops])