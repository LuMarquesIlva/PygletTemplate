from pyglet.input import *
from pyglet.app import exit

from Scripts.InputDefs import Keys

global updateInput

def updateInput(symbol = any, modifiers = any, OBJ_LIST = list, PREFERABLE_BOOL = bool) -> None:

    if getKeyName(symbol) == "ESCAPE":
        exit()
    print(OBJ_LIST)
    for OBJECT in OBJ_LIST:
        print(OBJECT.Name)
        match getKeyName(symbol):
            case "W":
                OBJECT.switchState(OBJECT.moveUp, PREFERABLE_BOOL)
                continue
            case "A":
                OBJECT.switchState(OBJECT.moveLeft, PREFERABLE_BOOL)
                #OBJECT()
                continue
            case "S":
               print(getKeyName(symbol))
               OBJECT.switchState(OBJECT.moveDown, PREFERABLE_BOOL)
               #OBJECT()
               continue
            case "D":
                OBJECT.switchState(OBJECT.moveRight, PREFERABLE_BOOL)
                #OBJECT()
                continue
            case _:
                pass
                
        


def getKeyName(KEY=int) -> str:
    return Keys.key[KEY]
