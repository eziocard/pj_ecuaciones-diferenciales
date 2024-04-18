import sys

import pygame
import sympy as sp
from matplotlib import pyplot as plt


class Metodo:
    def __init__(self,f,x0,y0,h,n):
        self.f = f
        self.x0 = x0
        self.y0 = y0
        self.h = h
        self.n = n

    errores = []

    def metodo_euler(self):
        k = sp.Symbol("k")
        y= sp.Symbol("y")
        x = sp.Symbol("x")
        val_x = [self.x0]
        val_y = [self.y0]

        for i in range(self.n):
            x_l = val_x[-1]
            y_l = val_y[-1]

            xnew = x_l + self.h
            ynew = y_l + self.h * self.f().evalf(subs={x:x_l,y:y_l,k:-0.02531780798})

            val_x.append(xnew)
            val_y.append(ynew)
        '''
        errores = []
        for x, y in zip(val_x, val_y):
            print(f'x = {x:.2f}, y= {y}')
            errores.append((100 + (-80) * sp.exp(-0.02531780798 * x)) - y)

        print(errores)

        promedio = sum(errores) / len(errores)'''
        return val_x,  val_y

    def metodo_taylor(self,orden):
        x = sp.Symbol("x")
        y = sp.Symbol("y")
        k = sp.Symbol("k")
        hs = sp.Symbol("hs")
        val_x = [self.x0]
        val_y = [self.y0]
        F = (self.f())
        Fs = []
        yformula = y
        for i in range(orden):
            Fs.append(F)
            F = sp.diff(F, "y") * self.f()  # regla de la cadena

        for p, q in enumerate(Fs):
            yformula += (hs ** p * q) / sp.factorial(p + 1)

        for i in range(self.n):
            xn = val_x[-1]
            yn = val_y[-1]

            xnew = xn + self.h
            ynew = yformula.evalf(subs={x: xn, y: yn, k: -0.02531780798, hs: self.h})

            val_x.append(xnew)
            val_y.append(ynew)
        '''
        errores =[]

        for x, y in zip(val_x, val_y):
            print(f'x = {x:.2f}, y= {y}')
            errores.append((100 + (-80) * sp.exp(-0.02531780798 * x)) - y)

        promedio = sum(errores) / len(errores)
        print("Error Promedio {}".format(promedio))'''
        return val_x, val_y

    def grafica_matplotlib(self,orden):
        eval_x,eval_y = self.metodo_euler()
        tval_x,tval_y = self.metodo_taylor(orden)
        plt.plot(eval_x, eval_y, linestyle="-.", label="metodo euler")
        plt.plot(tval_x, tval_y, linestyle="--", label="metodo taylor")
        plt.xlabel("Tiempo")
        plt.ylabel("Temperatura")
        plt.legend(["metodo euler", "metodo taylor"], loc=2)
        plt.title("Ley de enfriamiento")
        plt.show()


    def graficar(self,val_x,val_y):
        FPS = 3
        RELOJ = pygame.time.Clock()
        pygame.init()
        ventana = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ley de enfriamiento")

        blanco = (255, 255, 255)
        fondo = (88, 233, 242)
        negro = (0, 0, 0)
        aluminio = (201, 197, 193)
        font = pygame.font.Font(None, 36)
        fontcirculo = pygame.font.Font(None, 20)
        ventana.fill(blanco)

        cont = 0
        while True:

            cont = cont + 1
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
                    ventana.blit(texto_circulo, (347, 515))
                    pygame.draw.circle(ventana, negro, (390, 520), 80, 1)
                    color = 201+cont*3
                    if val_y[cont] > 50:
                        if 7 * cont < 255:
                            try:
                                pygame.draw.rect(ventana, (7 * cont, 160, 0), (50, 50, int(val_y[cont]) * 7, 20))
                                pygame.draw.rect(ventana, (7, 160, 0), (50, 50, int(val_y[cont]) * 7, 20))

                            except:
                                pygame.draw.rect(ventana, (7 * cont, 160, 0), (50, 50, int(val_y[cont]) * 7, 20))
                                pygame.draw.circle(ventana,(255, 197, 193), (390, 520), 80, 0)
                                pygame.draw.circle(ventana, negro, (390, 520), 80, 1)


                        else:
                            try:
                                pygame.draw.rect(ventana, (255, 160 - 7 * cont, 0), (50, 50, int(val_y[cont]) * 7, 20))

                            except:
                                pygame.draw.rect(ventana, (255, 0, 0), (50, 50, int(val_y[cont]) * 7, 20))


                    else:
                        pygame.draw.rect(ventana, (7 * cont, 160, 0), (50, 50, int(val_y[cont]) * 7, 20))
                    pygame.draw.rect(ventana, negro, (50, 50, 700, 20), 2)
                except Exception as e:
                    print(e)

            pygame.display.update()
            RELOJ.tick(FPS)


