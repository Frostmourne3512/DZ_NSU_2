a = int(input())
if 11 <= a <= 19:
    print(f'{a} попугаев')
b = a % 10
if b == 1:
    print(f'{a} попугай')
if 2 <= b <= 4:
    print(f'{a} попугая')
else:
    print(f'{a} попугаев')
