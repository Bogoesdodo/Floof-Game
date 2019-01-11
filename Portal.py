import arcade


class Portal(object):
    screenwidth = 0
    screenheight = 0
    portal_list = None
    portal_sprite = None
    current_room = 0
    def __init__(self, screenwidth, screenheight):
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        """
        This class holds all the information about the
        different rooms.
        """

    def setup_room_1():
        """
        Create and return room 1.
        If your program gets large, you may want to separate this into different
        files.
        """
        room = Room()

        """ Set up the game and initialize the variables. """
        # Sprite lists
        room.wall_list = arcade.SpriteList()

        # -- Set up the walls
        # Create bottom and top row of boxes
        # This y loops a list of two, the coordinate 0, and just under the top of window
        for y in (0, SCREEN_HEIGHT - SPRITE_SIZE):
            # Loop for each box going across
            for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
                wall = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

        # Create left and right column of boxes
        for x in (0, SCREEN_WIDTH - SPRITE_SIZE):
            # Loop for each box going across
            for y in range(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE, SPRITE_SIZE):
                # Skip making a block 4 and 5 blocks up on the right side
                if (y != SPRITE_SIZE * 4 and y != SPRITE_SIZE * 5) or x == 0:
                    wall = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING)
                    wall.left = x
                    wall.bottom = y
                    room.wall_list.append(wall)

        wall = arcade.Sprite("images/boxCrate_double.png", SPRITE_SCALING)
        wall.left = 7 * SPRITE_SIZE
        wall.bottom = 5 * SPRITE_SIZE
        room.wall_list.append(wall)

        # If you want coins or monsters in a level, then add that code here.

        # Load the background image for this level.
        room.background = arcade.load_texture("images/background.jpg")

        return room

    def setup_room_2():
        """
        Create and return room 2.
        """
        room = Room()

        """ Set up the game and initialize the variables. """
        # Sprite lists
        room.wall_list = arcade.SpriteList()

        # -- Set up the walls
        # Create bottom and top row of boxes
        # This y loops a list of two, the coordinate 0, and just under the top of window
        for y in (0, Game.SCREEN_HEIGHT - .04):
            # Loop for each box going across
            for x in range(0, Game.SCREEN_WIDTH, .04):
                wall = arcade.Sprite("images/boxCrate_double.png", .5)
                wall.left = x
                wall.bottom = y
                room.wall_list.append(wall)

        # Create left and right column of boxes
        for x in (0, Game.SCREEN_WIDTH - .04):
            # Loop for each box going across
            for y in range(.04, Game.SCREEN_HEIGHT - .04, .04):
                # Skip making a block 4 and 5 blocks up
                if (y != .04 * 4 and y != .04 * 5) or x != 0:
                    wall = arcade.Sprite("images/boxCrate_double.png", .5)
                    wall.left = x
                    wall.bottom = y
                    room.wall_list.append(wall)

        wall = arcade.Sprite("images/boxCrate_double.png", .5)
        wall.left = 5 * .04
        wall.bottom = 6 * .04
        room.wall_list.append(wall)
        room.background = arcade.load_texture("images/background_2.jpg")

        return room

    def roomlogic(self, delta_time):

        # Do some logic here to figure out what room we are in, and if we need to go
        # to a different room.
        if self.player_sprite.center_x > self.screenwidth and self.current_room == 0:
            self.current_room = 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 0
        elif self.player_sprite.center_x < 0 and self.current_room == 1:
            self.current_room = 0
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = Game.SCREEN_WIDTH



