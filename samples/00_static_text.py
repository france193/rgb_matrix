#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()

        font = graphics.Font()
        font.LoadFont("../fonts/6x9.bdf")

        text_green_color = graphics.Color(0, 128, 0)
        text_red_color = graphics.Color(128, 0, 0)
        text_blue_color = graphics.Color(0, 0, 128)
        text_color = graphics.Color(128, 128, 128)

        x_pos = 1

        y_pos_text_1 = 7
        y_pos_text_2 = y_pos_text_1 + 8
        y_pos_text_3 = y_pos_text_2 + 8
        y_pos_text_4 = y_pos_text_3 + 8

        text_1 = 'CIAO'
        text_2 = 'MONDO'
        text_3 = 'HELLO'
        text_4 = 'WORLD'

        while True:
            offscreen_canvas.Clear()

            graphics.DrawText(offscreen_canvas, font, x_pos, y_pos_text_1, text_color, text_1)
            graphics.DrawText(offscreen_canvas, font, x_pos, y_pos_text_2, text_red_color, text_2)
            graphics.DrawText(offscreen_canvas, font, x_pos, y_pos_text_3, text_green_color, text_3)
            graphics.DrawText(offscreen_canvas, font, x_pos, y_pos_text_4, text_blue_color, text_4)

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

    def print_help(self):
        pass


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if not run_text.process():
        run_text.print_help()
