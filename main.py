import pyglet
from pyglet import shapes

from Scripts.Core import Core
from Scripts.Entity import Object, Entity
from Scripts.Input import updateInput, Input

from Scripts.Display import DebugText

# Create window and batches
window = Core.InitWindow(800, 600)
batches = Core.CreateBatch() # Batch List

# Entity and Object declaration
Player = Entity("Player", batches[0].batchObj[0])
Enemy = Object("Enemy")

ObjList = [Player, Enemy] # Entity and Object Processing List

@window.event
def on_key_press(symbol, modifiers):
    updateInput(symbol, modifiers, ObjList, True)

@window.event
def on_key_release(symbol, modifiers):
    updateInput(symbol, modifiers, ObjList, False)

@window.event
def on_draw():
    Input.Update(ObjList) # Updates the States by Frame

    # Adds Debug Text to the screen
    label = DebugText(window, 10, window.height-10, 20, 
                      f"""MoveRight: {str(Player.moveRight.VALUE)}\nMoveLeft: {str(Player.moveLeft.VALUE)}\nMoveUp: {str(Player.moveUp.VALUE)}\nMoveDown: {str(Player.moveDown.VALUE)}\n\nPlayer_X: {str(Player.x)}\nPlayer_Y: {str(Player.y)}""", 
                      True).Text # Gets the Text Property

    # Clear the window and starts drawing
    window.clear()
    label.draw()

    batches[0].batchObj[0].draw() # Draw the batch in the list <batches: list | batchObj[index of the object]: Actual Batch>


    if Input.isPressed is True: # If is some key pressed

        # Update the Objects and Entities values
        Object.UpdateObjects(ObjList)
        inputCommand = Entity.UpdateEntities(ObjList)

        # If input is not None
        if inputCommand is not None:
            try:
                exec(inputCommand) # Execute Inputs
            except ValueError:
                print(ValueError)

pyglet.app.run()
