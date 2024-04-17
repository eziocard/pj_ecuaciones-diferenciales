import pygame
import math

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Crear la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cilindro en 3D en Pygame")

# Definir parámetros del cilindro
radius = 50
height = 150
num_segments = 30

# Función para proyectar un punto 3D a un punto 2D en la pantalla
def project_point(x, y, z):
    return x, y + z

# Función para dibujar un cilindro en 3D
def draw_cylinder_3d(surface, color, x, y, z, radius, height, num_segments):
    # Definir ángulo para cada segmento
    angle = 2 * math.pi / num_segments

    # Dibujar los lados del cilindro
    for i in range(num_segments):
        x_top = x + radius * math.cos(i * angle)
        y_top = y + radius * math.sin(i * angle)
        x_bottom = x + radius * math.cos((i + 1) * angle)
        y_bottom = y + radius * math.sin((i + 1) * angle)

        pygame.draw.line(surface, color, project_point(x_top, y_top, z), project_point(x_bottom, y_bottom, z + height))

    # Dibujar las bases del cilindro
    pygame.draw.circle(surface, color, project_point(x, y, z), radius)
    pygame.draw.circle(surface, color, project_point(x, y, z + height), radius)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la pantalla
    screen.fill(WHITE)

    # Dibujar el cilindro en 3D en el centro de la pantalla
    draw_cylinder_3d(screen, BLACK, WIDTH // 2, HEIGHT // 2, 0, radius, height, num_segments)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()