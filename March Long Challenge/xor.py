for te in range(int(input())):
    c = bin(int(input()))[2:]

    a = []
    b = []

    # int('11111111', 2)

    for i in range(len(c)):

        if c[i] == "0":
            a.append("1")
            b.append("1")
        else:
            if i == 0:
                a.append("1")
                b.append("0")
            else:
                a.append("0")
                b.append("1")

    print(int("".join(a), 2) * int("".join(b), 2))
