from pyglet.input import *
from pyglet.app import exit

from Scripts.InputDefs import Keys

global updateInput

class Input:
    
    isPressed = False # isPressed declaration


    def Update(STATE_LIST=list):
        for X in STATE_LIST: # for Every  item in the list
            for Y in X.StateList: # for every item in the StateList of the previous item
                if Y[0].VALUE is True: # if the State is True
                    Input.isPressed = True

# TODO: Add support for handling modifiers
def updateInput(symbol = any, modifiers = any, OBJ_LIST = list, PREFERABLE_BOOL = bool) -> None:

    # Get the key from the InputDefs and if it is ESCAPE, close application
    if getKeyName(symbol) == "ESCAPE":
        exit()
    
    # For every object in the list
    for OBJECT in OBJ_LIST:
        # Get the key and Switch the States accordingly
        match getKeyName(symbol):
            case "W":
                OBJECT.moveUp.switchState(PREFERABLE_BOOL)
                continue
            case "A":
                OBJECT.moveLeft.switchState(PREFERABLE_BOOL)
                continue
            case "S":
                OBJECT.moveDown.switchState(PREFERABLE_BOOL)
                continue
            case "D":
                OBJECT.moveRight.switchState(PREFERABLE_BOOL)
                continue
            case _:
                pass

def getKeyName(KEY=int) -> str:
    return Keys.key[KEY]
