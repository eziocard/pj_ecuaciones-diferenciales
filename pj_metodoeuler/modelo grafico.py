import pygame

import sys

pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("ley de enfriamiento")

"color del fondo"
blanco = (255,255,255)
rojo = (255,0,0)
negro = (0,0,0)
amarillo = 	(255, 255, 0)

"creacion de la tasa"
ventana.fill(blanco)
pygame.draw.rect(ventana,rojo,(350,499,100,100))
bar_x = 50
bar_y = 50
bar_width = 700
bar_height = 20
pygame.draw.rect(ventana, amarillo, (bar_x, bar_y, 60,bar_height))

# Dibuja el borde de la barra de carga
pygame.draw.rect(ventana, negro, (bar_x, bar_y, bar_width, bar_height), 2)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()