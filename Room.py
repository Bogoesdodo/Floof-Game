import arcade
import Decor
import NPC

rooms = []
wall = Decor.Decor("wall")
wall.spriteDeclare("sprites/wall.png", 0.24, 450, 550)
wall2 = Decor.Decor("wall2")
wall2.spriteDeclare("james.jpg", .24, 450, 550)
wall3 = Decor.Decor("wall")
wall3.spriteDeclare("sprites/wall.png", 0.24, 950, 250)
current_room = 0


class Room:
    wall_list = None
    background = None
    room_number = None

    def __init__(self):
        self.wall_list = None
        self.background = None
        self.room_number = None


def setup_room_0():
    """
        Create and return room 1.
        """
    room = Room()
    room.room_number = 0
    room.wall_list = arcade.SpriteList()

    #room.wall_list.append(wall.object_sprite)

    return room


def setup_room_1():
    room = Room()
    room.room_number = 1
    room.wall_list = arcade.SpriteList()

    room.wall_list.append(wall2.object_sprite)

    return room


def setup_room_2():
    room = Room()
    room.room_number = 2
    room.wall_list = arcade.SpriteList()

    room.wall_list.append(wall3.object_sprite)

    return room
