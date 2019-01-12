import arcade
import Room


class Portal(object):
    portal_list = None
    portal_sprite = None


    def __init__(self, screenwidth, screenheight):
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        """
        This class holds all the information about the
        different rooms.
        """
        self.current_room = 0

    def roomlogic(self, delta_time, player_sprite, physics_engine):

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if player_sprite.center_x > self.screenwidth and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(player_sprite, Room.rooms[self.current_room].wall_list)
            player_sprite.center_x = 0
        elif player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(player_sprite, Room.rooms[self.current_room].wall_list)
            player_sprite.center_x = self.screenwidth