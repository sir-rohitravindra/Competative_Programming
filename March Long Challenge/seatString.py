for t in range(int(input())):

    str=input()

    count=0
    frnd=0

    for i in range(len(str)):
        if(str[i]=="1" and not(frnd)):
            count+=1
            frnd=1
        elif(str[i]=="0"):
            frnd=0
    print(count)
