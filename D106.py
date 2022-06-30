ori = int(input())
u = ori % 10
u2 = ori % 100
if u2 >= 10 and u2 <= 20:
    print(f'{ori}th')
elif u == 1:
    print(f'{ori}st')
elif u == 2:
    print(f'{ori}nd')
elif u == 3:
    print(f'{ori}rd')
else:
    print(f'{ori}th')
