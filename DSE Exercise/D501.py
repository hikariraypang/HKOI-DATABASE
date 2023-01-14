f = open("account.txt", "r")
A = f.readline()
A = eval(A)
sum = 0
for X in range(A):
    B = f.readline()
    B = eval(B)
    sum = B + sum
print(sum)
