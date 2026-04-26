from pyglet.graphics import *

from Scripts.Input import *

# State Class: Used for easy creation of Finite State Machines
class State:
    NAME = ""
    VALUE = False
    
    
    # Constructor and instanciator -----
    def __init__(self, NAME=str):
        self.Name = NAME

    def __call__(self) -> State:
        return self
    # ----------------------------------
    
    def switchState(self) -> None:
        if self.VALUE==True:
            self.VALUE = False
        else:
            self.VALUE = True
    
        # Overload Method
    def switchState(self, STATEVAL=bool) -> None:
        if self.VALUE != STATEVAL:
            self.VALUE = STATEVAL

class Object:
    Name = ""

    x, y = 0.0, 0.0
    speed = 1
    
    moveUp = State("moveUp")
    moveDown = State("moveDown")
    moveRight = State("moveRight")
    moveLeft = State("moveLeft")
    
    StateList = [
        [moveUp, "{}.y -= {}.speed"],
        [moveDown, "{}.y += {}.speed"], 
        [moveRight, "{}.x += {}.speed"], 
        [moveLeft, "{}.x -= {}.speed"]
    ]


    # Constructor and instanciator -----
    def __init__(self, NAME=str):
        self.Name = NAME

    def __call__(self) -> Object:
        return self
    # ----------------------------------

    def UpdateObjects(OBJ_LIST=list):
        for XY in OBJ_LIST:
            for YZ in XY.StateList:
                Y = YZ[0] # StateList[0]
                Z = YZ[1] # StateList[1]

                if Y.VALUE is True:
                    Z = Z.format(XY.Name, XY.Name)
                    return Z # Return the formatted variable
        
                #print(f"{XY.Name} | {XY.x} | {XY.y}")
