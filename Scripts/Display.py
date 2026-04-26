from pyglet import text, window

class DebugText:

    Muliline = False

    Text = ""


    def __init__(self, DISPLAY_WINDOW=window ,xValue=float, yValue=float, SIZE=int, TEXT_VALUE=str, MULTILINE_MODE=bool):

        self.Muliline = MULTILINE_MODE

        if self.Muliline is True:
            label = text.Label(f"""{TEXT_VALUE}""",
                                width=DISPLAY_WINDOW.width//2,
                                multiline=self.Muliline,
                                font_name='Times New Roman',
                                font_size=SIZE,
                                x=xValue, y=yValue,
                                anchor_x='left', anchor_y='top')
        elif self.Muliline is False:
            label = text.Label(f"{TEXT_VALUE}",
                                width=DISPLAY_WINDOW.width//2,
                                multiline=self.Muliline,
                                font_name='Times New Roman',
                                font_size=SIZE,
                                x=xValue, y=yValue,
                                anchor_x='left', anchor_y='top')
            
        self.Text = label