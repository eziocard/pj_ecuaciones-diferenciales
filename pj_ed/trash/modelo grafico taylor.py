import sys
import matplotlib.pyplot as plt
import pygame
import sympy as sp


FPS = 3
RELOJ = pygame.time.Clock()


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
x0 = 1
y0 = 22
h = 1
n = 2000
orden = 5
val_x, val_y = Taylor(f, x0, y0, h, n, orden)

errores = []
for x, y in zip(val_x, val_y):
    print(f'x = {x:.2f}, y= {y}')
    errores.append((100 + (-80) * sp.exp(-0.02531780798 * x)) - y)

promedio = sum(errores) / len(errores)
print("Error Promedio {}".format(promedio))

'''  grafico de matplot lib
plt.plot(val_x,val_y)
plt.xlabel("Tiempo")
plt.ylabel("Temperatura")
plt.title("Ley de enfriamiento")
plt.show()
'''



pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("ley de enfriamiento")

blanco = (255,255,255)
fondo =(88, 233, 242)
rojo = (255,0,0)
negro = (0,0,0)
amarillo = 	(255, 255, 0)
posicion_texto = (100,100)
aluminio = (201, 197, 193 )
font = pygame.font.Font(None, 36)
fontcirculo = pygame.font.Font(None,20)
ventana.fill(blanco)


cont = 0
while True:

    cont = cont +1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if cont < len(val_y):
        ventana.fill(fondo)
        try:
            texto = font.render("Temperatura: {}".format(val_y[cont]), True, negro)
            ventana.blit(texto, (12, 15))
            pygame.draw.circle(ventana, aluminio, (390, 520), 80, 0)
            texto_circulo = fontcirculo.render("Barra aluminio", True, negro)
            ventana.blit(texto_circulo,(347,515))
            pygame.draw.circle(ventana, negro, (390, 520), 80, 1)

            if val_y[cont] > 50:
                if 7 * cont < 255:
                    pygame.draw.rect(ventana, (7 * cont, 160, 0), (50, 50,int(val_y[cont])*7, 20))
                else:
                    try:
                        pygame.draw.rect(ventana, (255, 160 - 7 * cont, 0), (50, 50, int(val_y[cont])*7, 20))
                    except:
                        pygame.draw.rect(ventana, (255, 0, 0), (50, 50, int(val_y[cont])*7, 20))

            else:
                pygame.draw.rect(ventana, (7 * cont, 160, 0), (50, 50, int(val_y[cont])*7, 20))
            pygame.draw.rect(ventana, negro, (50, 50, 700, 20), 2)


        except Exception as e:
            print("error {}".format(e))
            print(val_y[cont])


    pygame.display.update()
    RELOJ.tick(FPS)
