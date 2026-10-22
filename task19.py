n,m = map(int,input().split('x'))
k = int(input())
if (k % n == 0 and k % m != 0) or (k % m == 0 and k % n != 0):
    print('Da')
else:
    print('Net')