from __future__ import division
from selenium import webdriver

import numpy as np
from PIL import Image, ImageFont
from PIL import ImageDraw

class fakeCanvasHtml:

    driver = webdriver.PhantomJS()

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.words = list()

        self.img_grey = Image.new("L", (width, height))
        self.draw = ImageDraw.Draw(self.img_grey)
        self.img_array = np.asarray(self.img_grey)

    def getBoxSize(self, word, font_path, font_size, orientation):
        # returns the resulting size of the word with the font -> should be the same with HTML, right?

        # try to find a position
        font = ImageFont.truetype(font_path, font_size)
        # transpose font optionally
        transposed_font = ImageFont.TransposedFont(
            font, orientation=orientation)
        return self.draw.textsize(word, font=transposed_font)

    def drawText(self, xy, word, font_path, font_size, orientation, fill="white"):
        self.words.append((xy, word, font_path, font_size, orientation))
        # self.draw.text(xy, word, fill=fill, font=font)

    def getNpArray(self):
        html = self.generateHtml()
        with open("/tmp/word_cloud_html.html", "w") as tmpHtmlFile:
            tmpHtmlFile.write(html)
        #driver.set_window_size(1024, 768) # optional
        self.driver.get("file:///tmp/word_cloud_html.html")
        self.driver.save_screenshot('/tmp/word_cloud_screen.png')

        image = Image.open('/tmp/word_cloud_screen.png')

        return np.asarray(image)

    def generateHtml(self):
        result = '<!DOCTYPE html><html><head><link href="https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/html5resetcss/html5reset-1.6.1.css" rel="stylesheet">' + \
                 '<style>@font-face { font-family: "Droid Sans Mono"; font-style: normal; font-weight: 400; src: local("Droid Sans Mono"), local("DroidSansmono"), url("DroidSansMono.ttf"); }</style></head>' + \
                 '<body><ul style="width:' + str(self.width) + 'px; height: ' + str(
            self.height) + 'px; background-image:url(test.png); position: absolute; top:0;left:0;">\n'

        transform = ""
        for xy, word, font_path, font_size, orientation in self.words:
            rot = -90 if orientation else 0
            left = str(xy[0] + font_size if orientation else xy[0])
            top = str(xy[1] if orientation else xy[1] - font_size / 3)
            values = {
                "top": top,
                "left": left,
                "word": word,
                "font_size": font_size,
                "class": "rot" if orientation else "norm"
            }

            if orientation is not None:
                result += '<li style="background-color:rgba(255, 255, 255, 0.5); padding-left: 5.5em; display: inline; list-style: none; margin: 0; padding: 0;' + \
                          'font-family: \'Droid Sans Mono\', monospace;' + transform + 'position: absolute; top: ' + \
                          top + 'px; left: ' + left + 'px; font-size: ' + \
                          str(font_size) + 'px">' + word + '</li>\n'
                transform = "transform: rotate(-90deg); transform-origin: " + left + " " + top + " 0;"
                left = str(int(left) - font_size * 1.7)

            result += '<li style="background-color:rgba(255, 255, 255, 0.5); padding-left: 5.5em; display: inline; list-style: none; margin: 0; padding: 0;' + \
                      'font-family: \'Droid Sans Mono\', monospace;' + transform + 'position: absolute; top: ' + \
                      top + 'px; left: ' + left + 'px; font-size: ' + \
                      str(font_size) + 'px">' + word + '</li>\n'
        return result + "</ul></body>"