from pyglet.input import *
from pyglet.app import exit

from Scripts.InputDefs import Keys

global updateInput

class Input:
    
    isPressed = False


    def Update(STATE_LIST=list):
        for X in STATE_LIST:
            for Y in X.StateList:
                if Y[0].VALUE is True:
                    Input.isPressed = True

# TODO: Add support for handling modifiers
def updateInput(symbol = any, modifiers = any, OBJ_LIST = list, PREFERABLE_BOOL = bool) -> None:

    if getKeyName(symbol) == "ESCAPE":
        exit()
    
    for OBJECT in OBJ_LIST:
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
