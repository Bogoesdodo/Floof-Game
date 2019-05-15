import arcade
import time
import sys

delta_time = 0.0
# print text letter by letter
def delay_print(text, delay):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()
    print()

class displayText(object):
    text = ""
    text_list = None
    text_sprite = None
    display = False

    def __init__(self, text, x = None, y = None):
        self.text = text
        self.text_sprite = arcade.Sprite("sprites/textbox.png", .25)
        if x == None:
            self.text_sprite.center_x = 870
            self.text_sprite.center_y = 70
        else:
            self.text_sprite.center_x = x
            self.text_sprite.center_y = y





    def spriteDeclare(self, picture, size, x, y):

        self.text_sprite = arcade.Sprite(picture, size)
        self.text_sprite.center_x = x
        self.text_sprite.center_y = y


    def showDisplay (self, display):
        #makes texts into a array, Str = Array of strings "small sam" = "small", "sam"
        splitText = self.text.split()

        self.display = display
        self.text_list = arcade.SpriteList()
        self.text_list.append(self.text_sprite)

        if display :
            #delay_print(self.text, 1)
            self.text_list.draw()

            #draw text in textbox sprite
            arcade.draw_text(self.text, self.text_sprite.center_x - 30, self.text_sprite.center_y + 10, arcade.color.BLACK, 14)
