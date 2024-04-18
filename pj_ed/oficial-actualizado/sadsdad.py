import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Trapecio en Pygame")

vertices = [(100, 100), (200, 100), (250, 150), (50, 150)]
color = (255, 0, 0)  # Rojo (RGB)

pygame.draw.polygon(screen, color, vertices)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()