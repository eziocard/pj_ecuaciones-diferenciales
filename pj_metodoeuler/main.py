
import math


def mtd_euler(f,x0,y0,h,n):

    val_x = [x0]
    val_y = [y0]


    for i in range(n):
        x = val_x[-1]
        y = val_y[-1]

        yn = y + (h*f(x,y))

        xnew = x + h

        ynew = y + (h*(f(x,y) + f(xnew,yn)))/2

        val_x.append(xnew)
        val_y.append(ynew)


    return val_x, val_y

"colocar funcion"
def f(x,y):
    return 2*y*x

"colocar condiciones iniciales"
x0 =1
y0 = 1
h = 0.1
n = 5

val_x,val_y = mtd_euler(f,x0,y0,h,n)

for x,y in zip(val_x,val_y):
    print(f'x = {x:.2f}, y= {y:.4f}')
