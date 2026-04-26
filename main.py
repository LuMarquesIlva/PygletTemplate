import pyglet

from Scripts.Entity import Object
from Scripts.Input import updateInput

from Scripts.Display import DebugText

window = pyglet.window.Window(width=800, height=600)

Player = Object("Player")
Enemy = Object("Enemy")

ObjList = [Player, Enemy]

@window.event
def on_key_press(symbol, modifiers):
    updateInput(symbol, modifiers, ObjList, True)
    print(Player.x)

@window.event
def on_key_release(symbol, modifiers):
    updateInput(symbol, modifiers, ObjList, False)
    print(Player.x)

@window.event
def on_draw():
    label = DebugText(window, 10, window.height-10, 20, 
                      f"""MoveRight: {str(Player.moveRight.VALUE)}\nMoveLeft: {str(Player.moveLeft.VALUE)}\nMoveUp: {str(Player.moveUp.VALUE)}\nMoveDown: {str(Player.moveDown.VALUE)}""", True).Text

    '''
    label = pyglet.text.Label(f"""MoveRight: {str(Player.moveRight.VALUE)}\nMoveLeft: {str(Player.moveRight.VALUE)}\nMoveUp: {str(Player.moveUp.VALUE)}\nMoveDown: {str(Player.moveDown.VALUE)}""",
                          width=window.width//2,
                          multiline=True,
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
    '''
    window.clear()
    label.draw()

pyglet.app.run()
