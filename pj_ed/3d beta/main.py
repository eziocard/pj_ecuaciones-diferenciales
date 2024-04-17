import time

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
cont=1
app = Ursina(borderless=False)
time.dt = 1/30
random.seed(0)
window.size = (600, 600)

Entity.default_shader = lit_with_shadows_shader

usuario = FirstPersonController()


class Cubo(Entity):
    def __init__(self, position=(0, 0, 0),color=color.rgb(0,0,0),scale = (1,1)):
        super().__init__(position=position, model="/modelo/steelbeams/steelbeams.obj", scale=scale, origin_y=-.5, color=color,
                       collider="box")


usuario.position = Vec3(0, 2, 0)
ground = Entity(model='plane', collider='box', color=color.black, scale=64)
ground.position = (0, 1, 0)



def input(key):
    if key == 'escape':
        quit()
def update():
    for i in range(255):
        cubo = Cubo(position=(4, 0, 0), color=color.red)
        Sky()
        app.run()
        red = i
        green = 0
        blue = 0
        cubo.color=color.rgb(red,green,blue)
        time.sleep(1)



cubo = Cubo(position=(4, 0, 0), color=color.red)
Sky()

app.run()