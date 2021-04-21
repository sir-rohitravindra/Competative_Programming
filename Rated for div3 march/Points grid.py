for t in range(int(input())):

    n = int(input())

    l = [int(i) for i in input().split()]
    l.reverse()

    loops = l[0]
    cur = l[0] - 1

    for i in range(1, n):

        if cur >= l[i]:
            cur = l[i] - 1

        elif cur < l[i] and cur != 0:
            ncur = l[i] - cur
            cur=l[i]-1
            loops += ncur
        else:
            loops += l[i]
            cur=l[i]-1

    print(loops)
