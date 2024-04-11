import math
import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")

"colocar funcion"
def f(x,y):
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    return -x**2 * y

def factorial(n):
    resultado=1
    for i in range(1,n+1):
        resultado=resultado*i
    return resultado

def mtd_taylor(f,x0,y0,h,n):


    val_x = [x0]
    val_y = [y0]
    
    F=f(x,y)
    ynew= y

    for i in range(1,n+1):

        xn = val_x[-1]

        xnew = xn + h


        

        

        ynew+=((h**i)*F) / sp.factorial(i)

        print(ynew)

        ynew=ynew.evalf(subs={x:x0 , y:y0})

        F=(sp.diff(F,"x") + sp.diff(F,"y")*f(x,y))

        val_x.append(xnew)

        val_y.append(ynew)


    return val_x, val_y


"colocar condiciones iniciales"
x0 = 0
y0 = 0.3333
h = 1
n = 5

val_x,val_y = mtd_taylor(f,x0,y0,h,n)

for x,y in zip(val_x,val_y):
    print(f'x = {x}, y= {y}')