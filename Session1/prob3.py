for t in range(int(input())):
    input()
    l = [int(i) for i in input().split()]
    l.sort()
    m1 = l[-1]
    m2 = l[-2]

    s1 = l[0]
    s2 = l[1]
    a1 = (m1 * m2) + m1 - m2
    a2 = (s1 * s2) + s2 - s1
    print(max(a2, a1))

#Given an array A of size N. Find the maximum value of the expression a∗b+a−b
# where a and b are 2 distinct elements of the array.
