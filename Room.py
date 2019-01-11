import arcade
import Decor
rooms = []
wall = Decor.Decor("wall")
wall.spriteDeclare("wall.png", 0.24, 450, 550)

class Room:
    wall_list = None
    background = None

    def __init__(self):
        self.wall_list = None
        self.background = None

def setup_room_1():
    """
        Create and return room 2.
        """
    room = Room()

    room.wall_list = arcade.SpriteList()

    room.wall_list.append(wall.object_sprite)

    return room
