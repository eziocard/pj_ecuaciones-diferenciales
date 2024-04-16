from Metodo import Metodo
import sympy as sp


def f():
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    k = sp.Symbol("k")
    return k * (y - 100)

m = Metodo(f,0,20,1,2000)
m.metodo_euler()
m.metodo_taylor(5)


m.graficar(m.metodo_euler())
m.graficar(m.metodo_taylor(5))
