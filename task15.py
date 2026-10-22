n,k,m = map(int, input().split())
a = abs(m - k)
b = n - a
print(min(a,b))