from pyglet.input import *
from pyglet.app import exit

from Scripts.InputDefs import Keys

# State Class: Used for easy creation of Finite State Machines
class State:
    NAME = ""
    VALUE = False
    
    def __new__(self, name=str):
        self.NAME = name
        return self

    def switchState() -> None:
        if State.VALUE==True:
            State.VALUE = False
        else:
            State.VALUE = True


def updateInput(symbol = any, modifiers = any, OBJLIST = list) -> None:

    if getKeyName(symbol) == "ESCAPE":
        exit()
    
    for OBJECT in OBJLIST:
        match getKeyName(symbol):
            case "W":
                OBJECT.moveUp.switchState()
            case "A":
                OBJECT.moveLeft.switchState()
            case "S":
                OBJECT.moveDown.switchState()
            case "D":
                OBJECT.moveRight.switchState()
            case _:
                OBJECT._updateAllStatesInListToFalse()
                break
                

        OBJECT.Update()


def getKeyName(KEY=int) -> str:
    return Keys.key[KEY]

from Scripts.Entity import Object
