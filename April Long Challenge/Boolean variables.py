for t in range(int(input())):

    n,m,k=(int(i) for i in input().split())

    g=[int(i) for i in input().split()]
    dit=[]
    for i in range(m):
        tus=[int(i) for i in input().split()]
        dit.append(tus)
    scores=[]

    for i in range(2**n):
        arr=bin(i)[2:]
        if(len(arr)<n):
            arr="0"*(n-len(arr))+arr
        score=0
        for j in range(len(arr)):
            score+=int(arr[j])*g[j]
        for w in range(m):
            if not('0' in arr[dit[w][0]-1:dit[w][1]]):
                score+=dit[w][2]
        scores.append((score,arr))
    scores.sort(reverse=True)
    for ks in range(k):
        print(scores[ks])

"""for t in range(int(input())):

    n,m,k=(int(i) for i in input().split())
    gs=[int(i) for i in input().split()]
    g=[(gs[i],i) for i in range(len(gs))]

    d = []
    it = []
    for i in range(m):
        s = input().split()
        d.append(int(s[-1]))
        it.append((int(s[0]), int(s[1])))

    g.sort(reverse=True)
    sums=[]

    sumi = 0
    for v in range(n):
        sum = max(g[v][0], sumi+g[v][0])
        sums.append(sumi)
    sums.sort(reverse=True)
    for a in range(k):
        print(sums[a])"""

