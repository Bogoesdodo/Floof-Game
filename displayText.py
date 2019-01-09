import arcade

class displayText(object):
    text = ""
    text_list = None
    text_sprite = None
    display = False

    def __init__(self, text, x = None, y = None):
        self.text = text
        self.text_sprite = arcade.Sprite("textbox.png", 1)
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
        self.display = display
        self.text_list = arcade.SpriteList()
        self.text_list.append(self.text_sprite)
        if display :
            self.text_list.draw()
            arcade.draw_text(self.text, self.text_sprite.center_x - 30, self.text_sprite.center_y + 10, arcade.color.BLACK, 14)