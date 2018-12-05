from turtle import forward, left, right,exitonclick, setpos, up, down
from math import sqrt
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(3))

def koch(start_x,start_y,end_x,end_y,deph):
    if deph == 0:
        return
    dirx = (end_x-start_x)
    diry = (end_y-start_y)
    pointA = (start_x + dirx/3,start_y + diry/3)
    pointB = (start_x + 2*dirx / 3, start_y + 2*diry / 3)
    baseC = (start_x + dirx/2, start_y + diry/2)
    pointCx = baseC[0] - diry / 3 * sqrt(3)/2
    pointCy = baseC[1] + dirx / 3 * sqrt(3)/2
    setpos(start_x,start_y)
    down()
    setpos(pointA[0], pointA[1])
    setpos(pointCx, pointCy)
    setpos(pointB[0], pointB[1])
    setpos(end_x,end_y)
    up()

    koch(start_x, start_y, pointA[0], pointA[1], deph - 1)
    koch(pointA[0], pointA[1], pointCx, pointCy, deph - 1)
    koch(pointCx, pointCy, pointB[0], pointB[1], deph - 1)
    koch(pointB[0], pointB[1], end_x, end_y, deph - 1)


koch(0,0,50,50,2)

"""def vlocka(start_x,start_y,end_x,end_y,deph):
    base = sqrt((start_x-end_x)^2+(start_y-end_y)^2)
    dirx = (end_x-start_x)
    diry = (end_y-start_y)
    koch(start_x,start_y,end_x,end_y,deph)
    koch(end_x, end_y,(start_x+start_y)/2,base*sqrt(3), deph)
    #koch((start_x + start_y) / 2, base * sqrt(3),start_x,start_y, deph)

vlocka(0,0,5,50,2)"""
exitonclick()