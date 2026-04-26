import pyglet

from Scripts.Entity import Object
from Scripts.Input import updateInput, Input

from Scripts.Display import DebugText

window = pyglet.window.Window(width=800, height=600)

Player = Object("Player")
Enemy = Object("Enemy")

ObjList = [Player, Enemy]

@window.event
def on_key_press(symbol, modifiers):
    updateInput(symbol, modifiers, ObjList, True)

@window.event
def on_key_release(symbol, modifiers):
    updateInput(symbol, modifiers, ObjList, False)

@window.event
def on_draw():
    Input.Update(ObjList) # Updates the States by Frame

    label = DebugText(window, 10, window.height-10, 20, 
                      f"""MoveRight: {str(Player.moveRight.VALUE)}\nMoveLeft: {str(Player.moveLeft.VALUE)}\nMoveUp: {str(Player.moveUp.VALUE)}\nMoveDown: {str(Player.moveDown.VALUE)}""", 
                      True).Text # Gets the Text Property

    window.clear()
    label.draw()

    print(f"X {Player.x} | Y {Player.y}")
    if Input.isPressed is True:
        inputCommand = Object.UpdateObjects(ObjList)
        if inputCommand is not None:
            exec(inputCommand)

pyglet.app.run()
