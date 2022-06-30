X = int(input())
print(X)
while (X != 1):
    Y = X*0.5
    Z = Y//1
    if Z == Y:
        print('%d'%Y)
        X = Y
    else:
        P = 3*X+1
        print('%d'%P)
        X = P
