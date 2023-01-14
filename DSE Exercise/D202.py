import math
X = int(input())
A = int(math.sqrt(X))
for Y in range(1,A+1):
    if X % Y == 0:
        print(Y)
if A * A == X:
    A -= 1
for Y in range(A,0,-1):
    if X % Y == 0:
        print(X // Y)
