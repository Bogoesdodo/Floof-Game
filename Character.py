import arcade


class Hero(object):
    name = ""
    sex = ""
    movementSpeed = 5

    player_list = None
    player_sprite = None

    physics_engine = None




    def __init__(self, name, sex,):
        self.name = name
        self.sex = sex


        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None


