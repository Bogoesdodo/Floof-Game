#Starting Code


import config
import arcade
import os



SCREEN_WIDTH = 1150
SCREEN_HEIGHT = 950

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
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

        # initializing Sprite lists

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        #if key == arcade.key.UP:
           # self.player_sprite.change_y = MOVEMENT_SPEED
        #elif key == arcade.key.DOWN:
        #    self.player_sprite.change_y = -MOVEMENT_SPEED
        #elif key == arcade.key.LEFT:
         #   self.player_sprite.change_x = -MOVEMENT_SPEED
        #elif key == arcade.key.RIGHT:
            #self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        #if key == arcade.key.UP or key == arcade.key.DOWN:
        #    self.player_sprite.change_y = 0
       # elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
           # self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        #self.physics_engine.update()


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()