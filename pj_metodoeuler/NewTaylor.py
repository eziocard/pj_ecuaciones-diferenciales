import sympy as sp

def Taylor(f,x0,y0,h,n,orden):
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    k = sp.Symbol("k")
    hs = sp.Symbol("hs")
    val_x = [x0]
    val_y = [y0]
    F=(f())
    Fs=[]
    yformula = y
    for i in range(orden):
        Fs.append(F)
        F=sp.diff(F,"y")*f() #regla de la cadena

    for p,q in enumerate(Fs):
        yformula+=(hs**p*q)/(p+1)
    

    
    for i in range(n):
        xn = val_x[-1]
        yn = val_y[-1]

        xnew = xn + h
        ynew=yformula.evalf(subs={x:xn,y:yn,k:-0.02531780798,hs:h})


        val_x.append(xnew)
        val_y.append(ynew)


    return val_x, val_y

"colocar funcion"
def f():
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    k = sp.Symbol("k")
    return k*(y-100)

"colocar condiciones iniciales"
x0 = 1
y0 = 22
h = 1
n = 5
orden = 5
val_x,val_y = Taylor(f,x0,y0,h,n,orden)


errores = []
for x,y in zip(val_x,val_y):
    print(f'x = {x:.2f}, y= {y}')
    errores.append((100 + (-80) * sp.exp(-0.02531780798 * x))-y)

promedio = sum(errores)/len(errores)
print("Error Promedio {}".format(promedio))



