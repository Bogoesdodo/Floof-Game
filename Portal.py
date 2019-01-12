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




    def roomlogic(self, delta_time, player_sprite, physics_engine, room1, room2, side):

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if side == "right":
            if player_sprite.center_x > self.screenwidth and Room.current_room == room1:
                Room.current_room = room2
                self.physics_engine = arcade.PhysicsEngineSimple(player_sprite, Room.rooms[Room.current_room].wall_list)
                player_sprite.center_x = 0
            elif player_sprite.center_x < 0 and Room.current_room == room2:
                Room.current_room = room1
                self.physics_engine = arcade.PhysicsEngineSimple(player_sprite, Room.rooms[Room.current_room].wall_list)
                player_sprite.center_x = self.screenwidth

        elif side == "left":
            if player_sprite.center_x < 0 and Room.current_room == room1:
                Room.current_room = room2
                self.physics_engine = arcade.PhysicsEngineSimple(player_sprite, Room.rooms[Room.current_room].wall_list)
                player_sprite.center_x = self.screenwidth
            elif player_sprite.center_x > self.screenwidth and Room.current_room == room2:
                Room.current_room = room1
                self.physics_engine = arcade.PhysicsEngineSimple(player_sprite, Room.rooms[Room.current_room].wall_list)
                player_sprite.center_x = 0