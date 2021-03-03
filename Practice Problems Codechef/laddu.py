for t in range(int(input())):
    n, k = [int(i) for i in input().split()]

    l = [int(i) for i in input().split()]
    l.sort()
    difs = [l[i + 1] - l[i] for i in range(len(l) - 1)]

    difs.sort()
    print(difs)
    print(difs[0:k-1])
    print(sum(difs[0:k - 1]))
# cook your dish here
