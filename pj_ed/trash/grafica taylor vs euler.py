import sympy as sp
import matplotlib.pyplot as plt

def Taylor(f, x0, y0, h, n, orden):
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    k = sp.Symbol("k")
    hs = sp.Symbol("hs")
    val_x = [x0]
    val_y = [y0]
    F = (f())
    Fs = []
    yformula = y
    for i in range(orden):
        Fs.append(F)
        F = sp.diff(F, "y") * f()  # regla de la cadena

    for p, q in enumerate(Fs):
        yformula += (hs ** p * q) / (p + 1)

    for i in range(n):
        xn = val_x[-1]
        yn = val_y[-1]

        xnew = xn + h
        ynew = yformula.evalf(subs={x: xn, y: yn, k: -0.02531780798, hs: h})

        val_x.append(xnew)
        val_y.append(ynew)

    return val_x, val_y


"colocar funcion"


def f():
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    k = sp.Symbol("k")
    return k * (y - 100)


"colocar condiciones iniciales"
x0 = 0
y0 = 20
h = 1
n = 250
orden = 5
val_x, val_y = Taylor(f, x0, y0, h, n, orden)

tval_x, tval_y = Taylor(f, x0, y0, h, n, orden)

errores = []
for x, y in zip(val_x, val_y):
    print(f'x = {x:.2f}, y= {y}')

    errores.append((100 + (-80) * sp.exp(-0.02531780798 * x)) - y)

promedio = sum(errores) / len(errores)
print("Error Promedio {}".format(promedio))




'metod de euler'
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
    return -0.02531780798*(y-100)

"colocar condiciones iniciales"
x0 =0
y0 = 20
h = 1
n = 250

val_x,val_y = mtd_euler(f,x0,y0,h,n)
eval_x,eval_y = mtd_euler(f,x0,y0,h,n)
for x,y in zip(val_x,val_y):
    print(f'x = {x:.2f}, y= {y:.4f}')




def mtd_analitico(rangoDeX):

    val_x = []
    val_y = []


    for i in range(rangoDeX+1):

        ynew=100 + (-80) * sp.exp(-0.02531780798 * i)


        val_x.append(i)
        val_y.append(ynew)


    return val_x, val_y

"colocar funcion"
def f(x,y):
    return -0.02531780798*(y-100)

"colocar condiciones iniciales"
rangoDeX = 250

val_x,val_y = mtd_analitico(rangoDeX)
aval_x,aval_y = mtd_analitico(rangoDeX)
for x,y in zip(val_x,val_y):
    print(f'x = {x:.2f}, y= {y}')


plt.plot(eval_x,eval_y, linestyle = "-.",label = "metodo euler" )
plt.plot(tval_x,tval_y,linestyle = "--", label = "metodo taylor")
plt.plot(aval_x,aval_y,linestyle = ":")
plt.xlabel("Tiempo")
plt.ylabel("Temperatura")
plt.legend(["metodo euler","metodo taylor","metodo analitico"],loc=2)
plt.title("Ley de enfriamiento")
plt.show()



