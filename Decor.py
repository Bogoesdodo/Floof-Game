import arcade

class Decor(object):
    #draw tree and what the fuck not
    object = ""
    object_list = None
    object_sprite = None
    physics_engine = None


    def __init__(self, object):
        self.object = object

        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None

    def spriteDeclare(self, picture, size, x, y):
        self.object_list = arcade.SpriteList()
        self.object_sprite = arcade.Sprite(picture, size)
        self.object_sprite.center_x = x
        self.object_sprite.center_y = y




