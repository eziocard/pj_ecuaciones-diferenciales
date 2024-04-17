from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=False)
window.size = (600, 600)
Entity.default_shader = lit_with_shadows_shader

usuario = FirstPersonController()

class Cubo(Entity):
    def __init__(self, position=(0, 0, 0), color=color.rgb(0, 0, 0), scale=(1, 1)):
        super().__init__(
            position=position,
            model="/modelo/steelbeams/steelbeams.obj",
            scale=scale,
            origin_y=-.5,
            color=color,
            collider="box"
        )

usuario.position = Vec3(0, 2, 0)
ground = Entity(model='plane', collider='box', color=color.black, scale=64)
ground.position = (0, 1, 0)

cubo = Cubo(position=(4, 0, 0), color=color.rgb(0, 0, 0))

def change_color():
    global cont
    r = min(255, cubo.color.r + 1)
    g = min(255, cubo.color.g + 0.5)
    b = min(255, cubo.color.b + 0.2)
    cubo.color = color.rgb(r, g, b)

def update():
    change_color()

def input(key):
    if key == 'escape':
        quit()

Sky()
app.run()