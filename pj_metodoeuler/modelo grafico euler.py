import sys
import matplotlib.pyplot as plt
import pygame
import sympy as sp


FPS = 3
RELOJ = pygame.time.Clock()

def mtd_euler(f,x0,y0,h,n):

    val_x = [x0]
    val_y = [y0]


    for i in range(n):
        x = val_x[-1]
        y = val_y[-1]

        xnew = x + h
        ynew = y + h*f(x,y)

        val_x.append(xnew)
        val_y.append(ynew)


    return val_x, val_y

"colocar funcion"
def f(x,y):
    return -0.02531780798*(y-100)

"colocar condiciones iniciales"
x0 = 0
y0 = 20
h = 1
n = 2000


val_x,val_y = mtd_euler(f,x0,y0,h,n)
errores = []
for x,y in zip(val_x,val_y):
    print(f'x = {x:.2f}, y= {y:2f}')
    errores.append((100 + (-80) * sp.exp(-0.02531780798 * x))-y)

print(errores)

promedio = sum(errores)/len(errores)
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
                if 7*cont < 255:
                    pygame.draw.rect(ventana, (7*cont, 160, 0), (50, 50, val_y[cont]*7, 20))

                else:
                    try:
                        pygame.draw.rect(ventana, (255, 160-7*cont, 0), (50, 50, val_y[cont] * 7, 20))
                    except:
                        pygame.draw.rect(ventana, (255,0, 0), (50, 50, val_y[cont] * 7, 20))

            else:
                pygame.draw.rect(ventana, (7*cont,160,0), (50, 50, val_y[cont] * 7, 20))
            pygame.draw.rect(ventana, negro, (50, 50, 700, 20), 2)
        except:
            print("error")


    pygame.display.update()
    RELOJ.tick(FPS)
