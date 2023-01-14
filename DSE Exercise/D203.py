Num = int (input ())
for X in range (0, 10):
    A = ''
    for Y in range (1, 11):
        B = str(X * 10 + Y)
        C = ' '
        Nums = str(Num)
        if len(B.split (Nums)) >= 2:
            A = A + 'Clap '
        elif (X * 10 + Y) % Num == 0:
            A = A + 'Clap '
        else:
            A = A + B + C
    print (A)
