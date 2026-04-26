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

# Object class: Mainly for basic shapes and movement
class Object:
    Name = ""

    x, y = 0.0, 0.0 # Object Position
    speed = 3.5 # Object Speed
    
    # States declarations: Basically my attempt at Finite State Machines by guessing what it is ----
    moveUp = State("moveUp")
    moveDown = State("moveDown")
    moveRight = State("moveRight")
    moveLeft = State("moveLeft")
    
    StateList = [
        [moveUp, "{}.y += {}.speed"],
        [moveDown, "{}.y -= {}.speed"], 
        [moveRight, "{}.x += {}.speed"], 
        [moveLeft, "{}.x -= {}.speed"]
    ]

    # ------------------------------------------------------------------------------------------------

    # Constructor and instanciator -----
    def __init__(self, NAME=str):
        self.Name = NAME

    def __call__(self) -> Object:
        return self
    # ----------------------------------

    def UpdateObjects(OBJ_LIST=list):
        for XY in OBJ_LIST: # For every object on the list
            for YZ in XY.StateList: # Get the StateList for them
                Y = YZ[0] # StateList[0]
                Z = YZ[1] # StateList[1]

                if Y.VALUE is True: # If the State is True
                    Z = Z.format(XY.Name, XY.Name) # Format the Name of it to use with the action
                    return Z # Return the formatted variable
                

class Entity(Object):
    Name=""
    Shape = pyglet.shapes.ShapeBase # Shape Declaration


    # Constructor ----
    def __init__(self, Name=str, _BATCH=pyglet.graphics.Batch):
        self.Name = Name
        self.Shape = pyglet.shapes.Rectangle(self.x, self.y, 50, 80, color=(100, 22, 20), batch=_BATCH)
    # ---------------


    def UpdateEntities(ENT_LIST=list):
        for XY in ENT_LIST: # For every Item on the list
            if type(XY) is Entity:  # If it's type is Entity
                
                # Update the Position Values
                XY.Shape.x = XY.x 
                XY.Shape.y = XY.y


                for YZ in XY.StateList: # Get the StateLis
                    Y = YZ[0] # StateList[0]
                    Z = YZ[1] # StateList[1]

                    if Y.VALUE is True: # If the State is True
                        Z = Z.format(XY.Name, XY.Name) # Format the action
                        return Z # Return the formatted variable
            else:
                pass
