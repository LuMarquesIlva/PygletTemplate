import pyglet

from Scripts.Input import *

window = pyglet.window.Window(width=800, height=600)

label = pyglet.text.Label('Olá, Mundo!',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

Player = Object()

ObjList = [Player]

@window.event
def on_key_press(symbol, modifiers):
    updateInput(symbol, modifiers, ObjList)
    print(Player.x)

@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()
