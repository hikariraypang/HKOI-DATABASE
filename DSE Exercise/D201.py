A = int(input())
if A == 0:
    print(0)

else:
    S = 0
    Y = 1
    for X in range(A):
        Z = S+Y
        Y = S
        S = Z
    print(Z)
