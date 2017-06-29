from __future__ import division

import numpy as np
from PIL import Image
from PIL import ImageDraw

from PIL import ImageFont


class fakeCanvasImg:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.img_grey = Image.new("L", (width, height))
        self.draw = ImageDraw.Draw(self.img_grey)
        self.img_array = np.asarray(self.img_grey)

    def getBoxSize(self, word, font_path, font_size, orientation):

        # try to find a position
        font = ImageFont.truetype(font_path, font_size)
        # transpose font optionally
        transposed_font = ImageFont.TransposedFont(
            font, orientation=orientation)
        return self.draw.textsize(word, font=font)

    def drawText(self, xy, word, font_path, font_size, orientation, fill="white"):
        # try to find a position
        font = ImageFont.truetype(font_path, font_size)
        # transpose font optionally
        transposed_font = ImageFont.TransposedFont(
            font, orientation=orientation)
        self.draw.text(xy, word, fill=fill, font=font)

    def getNpArray(self):
        return np.asarray(self.img_grey)
