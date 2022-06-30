N = int( input( ) )
C1 = N // 1000
if  C1 > 0:
    for n in range(C1):
        print('1000')
    N = N-(C1*1000)
C2 = N // 500
if  C2 > 0:
    for n in range(C2):
        print('500')
    N = N - (C2 * 500)
C3 = N // 100
if  C3 > 0:
    for n in range(C3):
        print('100')
    N = N - (C3 * 100)
C4 = N // 50
if  C4 > 0:
    for n in range(C4):
        print('50')
    N = N - (C4 * 50)
C5 = N // 20
if  C5 > 0:
    for n in range(C5):
        print('20')
    N = N - (C5 * 20)
C6 = N // 10
if  C6 > 0:
    for n in range(C6):
        print('10')
