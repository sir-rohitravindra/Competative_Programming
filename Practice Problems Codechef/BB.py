# cook your dish here
for te in range(int(input())):
    (x, y) = [int(i) for i in input().split()]

    print((x,y))
    if x == y:
        print(0)
    elif x < y:
        if ((y - x) % 2 != 0):
            print(1)
        else:
            print(2)
    else:
        if (x-y) % 2 == 0:
            print(1)
        else:
            print(2)

