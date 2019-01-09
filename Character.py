import arcade


class Hero(object):
    name = ""
    sex = ""
    movementSpeed = 5

    health = 100
    strength = 5
    dexterity = 5
    intelligence = 5
    luck = 5


    player_list = None
    player_sprite = None
    physics_engine = None




    def __init__(self, name, sex,):
        self.name = name
        self.sex = sex


        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None

    def spriteDeclare(self, picture, size, x, y):
        player_list = arcade.SpriteList()
        player_sprite = arcade.Sprite(picture,size)
        player_sprite.center_x = x
        player_sprite.center_y = y
        player_list.append(player_sprite)

