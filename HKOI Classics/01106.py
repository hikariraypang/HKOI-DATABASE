A = eval(input())
N = eval(input())
C = 0
for r in range(N):
    M = eval(input())
    A = A-M
    while 0 >= A:
        A = A + 250
        C = C + 250
print('$%.d'%C)
