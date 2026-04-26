from pyglet.graphics import *

from Scripts.Input import State

class Object:
    x, y = 0.0, 0.0
    speed = 5
    
    moveUp = State("moveUp")
    moveDown = State("moveDown")
    moveRight = State("moveRight")
    moveLeft = State("moveLeft")
    
    StateList = [
        [moveUp, "Object.y -= Object.speed"], 
        [moveDown, "Object.y += Object.speed"], 
        [moveRight, "Object.x += Object.speed"], 
        [moveLeft, "Object.x -= Object.speed"]
    ]

    def __new__(self) -> Object:
         return self
    
    def _updateStateList(STATELIST = list):
        for States in STATELIST:
            match States[0].NAME:
                case "moveUp":
                    States[0] = Object.moveUp
                case "moveDown":
                    States[0] = Object.moveDown
                case "moveRight":
                    States[0] = Object.moveRight
                case "moveLeft":
                    States[0] = Object.moveLeft

    def _updateAllStatesInListToFalse():
        for States in Object.StateList:
            match States[0].NAME:
                case "moveUp":
                    if States[0].VALUE == True:
                        States[0] = Object.moveUp.switchState()
                case "moveDown":
                    if States[0].VALUE == True:
                        States[0] = Object.moveDown.switchState()
                case "moveRight":
                    if States[0].VALUE == True:
                        States[0] = Object.moveRight.switchState()
                case "moveLeft":
                    if States[0].VALUE == True:
                        States[0] = Object.moveLeft.switchState()

        ind = 0
        
        for Y in Object.StateList:
            stateString = ""

            if ind == 0:
                stateString = str(Y[0].VALUE) + " ,"
                ind += 1
            else:
                stateString += str(Y[0].VALUE) + " -"

            print(stateString)
                    

    def Update() -> None:
        Object._updateStateList(Object.StateList)

        for x in Object.StateList:
            match x[0].VALUE:
                case True:
                    exec(x[1])
                case False:
                    break