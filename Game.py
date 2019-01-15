# Starting Code


import os
import displayText
import arcade
import Decor
import Character
import Portal
import Room
import NPC

SCREEN_WIDTH = 950
SCREEN_HEIGHT = 700

text1 = displayText.displayText("aaron is aaron")

port = Portal.Portal(SCREEN_WIDTH, SCREEN_HEIGHT)

hero = Character.setup_player()

boy1 = NPC.setup_npc0()

room0 = Room.setup_room_0()
Room.rooms.append(room0)
room1 = Room.setup_room_1()
Room.rooms.append(room1)
room2 = Room.setup_room_2()
Room.rooms.append(room2)


class MyGame(arcade.Window):
    """ Main application class. """
    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        # Sprite lists

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Set the background color
        arcade.set_background_color(arcade.color.ANTI_FLASH_WHITE)
        # Set up the Sprites



        # make the two sprites interact
        hero.physics_engine = arcade.PhysicsEngineSimple(hero.player_sprite, Room.rooms[Room.current_room].wall_list)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        arcade.draw_rectangle_filled(100, 200, 50, 80, arcade.color.YELLOW)
        hero.player_list.draw()

        text1.showDisplay((hero.player_sprite._get_center_y() > 40))
        NPC.interact(arcade.get_distance_between_sprites(hero.player_sprite, boy1.npc_sprite))
        boy1.npc_sprite.draw()
        # Draw the rooms

        Room.rooms[Room.current_room].wall_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            hero.player_sprite.change_y = hero.movementSpeed
        elif key == arcade.key.DOWN:
            hero.player_sprite.change_y = -hero.movementSpeed
        elif key == arcade.key.LEFT:
            hero.player_sprite.change_x = -hero.movementSpeed
        elif key == arcade.key.RIGHT:
            hero.player_sprite.change_x = hero.movementSpeed

        if key == arcade.key.W:
            boy1.npc_sprite.change_y = hero.movementSpeed
        elif key == arcade.key.S:
            boy1.npc_sprite.change_y = -hero.movementSpeed
        elif key == arcade.key.A:
            boy1.npc_sprite.change_x = -hero.movementSpeed
        elif key == arcade.key.D:
            boy1.npc_sprite.change_x = hero.movementSpeed

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            hero.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            hero.player_sprite.change_x = 0
        if key == arcade.key.W or key == arcade.key.S:
            boy1.npc_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            boy1.npc_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        hero.physics_engine.update()
        hero.player_list.update()
        hero.player_list.update_animation()
        boy1.npc_list.update()
        boy1.npc_list.update_animation()

        port.roomlogic(delta_time, hero.player_sprite, room0.room_number, room1.room_number, "right")
        port.roomlogic(delta_time, hero.player_sprite, room0.room_number, room2.room_number, "bottom")
        hero.physics_engine = arcade.PhysicsEngineSimple(hero.player_sprite, Room.rooms[Room.current_room].wall_list)




def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
