from turtle import *
xc,yc,r,x,y = map(int,input().split())
circle(r,xc,yc)
d = ((xc - x) ** 2 + (yc - y) ** 2)**0.5
if d < r:
    print('Точка внутри круга')
if d == r:
    print('Точка на круге')
if d > r:
    print('Точка вне круга')
