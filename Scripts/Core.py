import pyglet

class _batch:
    batchObj = tuple # (Batch, ID)
    TotalBatches = 0 # Total number of batches GLOBAL

    # Constructor ---
    def __init__(self):
        self.batchObj = (pyglet.graphics.Batch(), self.TotalBatches)
        self.TotalBatches += 1
    
    def __call__(self):
        return self.batchObj
    # ---------------


class Core:
    window = None # Window Def
    batches = [] # Batches list for multiple batches support

    # Create batch an append it to the list
    def CreateBatch():
        Core.batches.append(_batch())
        return Core.batches

    # Create the window and update the variable
    def InitWindow(width=int, height=int):
        Core.window = pyglet.window.Window(width, height)
        return Core.window
