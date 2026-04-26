from pyglet.input import *

from Scripts.InputDefs import Keys

def switchState(STATE=bool) -> None:
    if STATE==True:
        STATE = False
    else:
        STATE = True

def getKeyName(KEY=int) -> str:
    return Keys.key[KEY]
