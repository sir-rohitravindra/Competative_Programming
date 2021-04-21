for t in range(100):

    s=bin(t)[2:]
    for i in range(1024):
        ss=bin(i)[2:]
        #print("substring ## ",ss)
        k=0
        j=0
        while k<len(ss) and j<len(s):
            if(ss[k]==s[j]):
                k+=1
            j+=1
        if(k!=len(ss)):
            print((s,ss),(int(s,2),int(ss,2)),int(s,2)^int(ss,2))
            #print(t,",",int(ss,2))

            break
"""a=sys.maxsize
print(a)"""