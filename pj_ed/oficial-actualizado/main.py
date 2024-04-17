import sys

import pygame
from pygame.locals import *

from Metodo import Metodo
import sympy as sp


def f():
    x = sp.Symbol("x")
    y = sp.Symbol("y")
    k = sp.Symbol("k")
    return k * (y - 100)

m = Metodo(f,0,20,1,2000)
#m.metodo_euler()
#m.metodo_taylor(5)


#m.graficar(m.metodo_euler())
#m.graficar(m.metodo_taylor(5))

pygame.init()

Pantalla = pygame.display.set_mode((600,600))
pygame.display.set_caption("MENU")
euler = pygame.Rect(220,220,200,50)
taylor = pygame.Rect(220,300,200,50)
font = pygame.font.Font(None,32)

while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if euler.collidepoint(pygame.mouse.get_pos()):
                m.metodo_euler()
                m.graficar(m.metodo_euler())

            if taylor.collidepoint(pygame.mouse.get_pos()):
                m.metodo_taylor(5)
                m.graficar(m.metodo_taylor(5))
                print("2")

    Pantalla.fill((255, 255, 255))
    pygame.draw.rect(Pantalla,(100,100,100),euler,0)
    pygame.draw.rect(Pantalla, (100, 100, 100),taylor, 0)
    txt_1 = font.render("Metodo de euler",True,(255,255,255))
    txt_2 = font.render("Metodo de Taylor", True, (255, 255, 255))
    Pantalla.blit(txt_1,(euler.x+(euler.width-txt_1.get_width())/2,euler.y+(euler.height-txt_1.get_height())/2))
    Pantalla.blit(txt_2,(taylor.x+(taylor.width-txt_2.get_width())/2,taylor.y+(taylor.height-txt_2.get_height())/2))
    pygame.display.update()