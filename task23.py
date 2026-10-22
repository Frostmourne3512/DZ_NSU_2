from math import *
n = int(input())
if n == 1:
    print(0)
if n < 11 and n != 1:
    print(n-1)
if 190 > n > 10:
    n = n - 10
    a = ceil(n / 2)
    b = n % 2
    if b == 1:
        print((10 + a - 1) // 10)
    if b != 1:
        print((10 + a - 1) % 10)
if n > 190:
    n = n - 190
    a = ceil(n / 3)
    b = n % 3
    if b == 1:
        print((190 + a - 1) // 100)
    if b == 2:
        print((190 + a - 1) % 10 // 10)
    if b == 0:
        print((190 + a - 1) % 10)


