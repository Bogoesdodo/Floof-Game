import arcade

class displayText(object):
    text = ""
    text_list = None
    text_sprite = None
    display = False
    def __init__(self, text):
        self.text = text

    def spriteDeclare(self, picture, size, x, y):
        self.text_list = arcade.SpriteList()
        self.text_sprite = arcade.Sprite(picture, size)
        self.text_sprite.center_x = x
        self.text_sprite.center_y = y
        self.text_list.append(self.text_sprite)

    def showDisplay (self, display):
        self.display = display
        if display :
            self.text_list.draw()
