from pyglet.graphics import *

from Scripts.Input import *

# State Class: Used for easy creation of Finite State Machines
class State:
    NAME = ""
    VALUE = False
    
    def __new__(self, name=str):
        self.NAME = name
        return self

class Object:
    Name = ""

    x, y = 0.0, 0.0
    speed = 5
    
    moveUp = State("moveUp")
    moveDown = State("moveDown")
    moveRight = State("moveRight")
    moveLeft = State("moveLeft")
    
    StateList = [
        [moveUp, "self.y -= self.speed"],
        [moveDown, "self.y += self.speed"], 
        [moveRight, "self.x += self.speed"], 
        [moveLeft, "self.x -= self.speed"]
    ]

    def __new__(self, NAME=str) -> Object:
         self.Name = NAME
         return self
    
    def switchState(self) -> None:
        if self.VALUE==True:
            self.VALUE = False
        else:
            self.VALUE = True
    
    # Overload Method
    def switchState(self, STATEVAL=bool) -> None:
        if self.VALUE != STATEVAL:
            self.VALUE = STATEVAL
    
    '''
            def __call__(self):
        for State in self.StateList:
            if State[0].Value is True:
                exec(State[1]) 
    '''
