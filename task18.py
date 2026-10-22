a,b,c,d,e = map(int,input().split())
g = []
g.append(c)
g.append(d)
g.append(e)
g.sort()
if g[0] <= min(a,b) and g[1] <= max(a,b):
    print('Yes')
else:
    print('No')