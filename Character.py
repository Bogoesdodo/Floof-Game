import arcade
import Room

class Hero(object):
    name = ""
    gender = ""
    movementSpeed = 1

    health = 100
    strength = 5
    dexterity = 5
    intelligence = 5
    luck = 5
    space_key = False
    player_list = None
    player_sprite = None
    physics_engine = None

    def __init__(self, name, sex ):
        self.name = name
        self.sex = sex

        self.player_sprite = None
        self.player_list = None
        self.physics_engine = None

def setup_player():
    size = 10
    char = Hero("Steven","girl")
    char.player_list = arcade.SpriteList()
    char.player_sprite = arcade.AnimatedWalkingSprite()

    char.player_sprite.stand_right_textures = []
    char.player_sprite.stand_right_textures.append(arcade.load_texture("sprites/Male player/right.png", scale=size))

    char.player_sprite.stand_left_textures = []
    char.player_sprite.stand_left_textures.append(arcade.load_texture("sprites/Male player/left.png", scale=size))

    char.player_sprite.walk_right_textures = []
    char.player_sprite.walk_right_textures.append(arcade.load_texture("sprites/Male player/right1.png", scale=size))
    char.player_sprite.walk_right_textures.append(arcade.load_texture("sprites/Male player/right2.png", scale=size))
    char.player_sprite.walk_right_textures.append(arcade.load_texture("sprites/Male player/right1.png", scale=size))
    char.player_sprite.walk_right_textures.append(arcade.load_texture("sprites/Male player/right2.png", scale=size))

    char.player_sprite.walk_left_textures = []
    char.player_sprite.walk_left_textures.append(arcade.load_texture("sprites/Male player/left1.png", scale=size))
    char.player_sprite.walk_left_textures.append(arcade.load_texture("sprites/Male player/left2.png", scale=size))
    char.player_sprite.walk_left_textures.append(arcade.load_texture("sprites/Male player/left1.png", scale=size))
    char.player_sprite.walk_left_textures.append(arcade.load_texture("sprites/Male player/left2.png", scale=size))

    char.player_sprite.walk_up_textures = []
    char.player_sprite.walk_up_textures.append(arcade.load_texture("sprites/Male player/up1.png", scale=size))
    char.player_sprite.walk_up_textures.append(arcade.load_texture("sprites/Male player/up2.png", scale=size))
    char.player_sprite.walk_up_textures.append(arcade.load_texture("sprites/Male player/up1.png", scale=size))
    char.player_sprite.walk_up_textures.append(arcade.load_texture("sprites/Male player/up2.png", scale=size))

    char.player_sprite.walk_down_textures = []
    char.player_sprite.walk_down_textures.append(arcade.load_texture("sprites/Male player/down1.png", scale=size))
    char.player_sprite.walk_down_textures.append(arcade.load_texture("sprites/Male player/down2.png", scale=size))
    char.player_sprite.walk_down_textures.append(arcade.load_texture("sprites/Male player/down1.png", scale=size))
    char.player_sprite.walk_down_textures.append(arcade.load_texture("sprites/Male player/down2.png", scale=size))

    char.player_sprite.texture_change_distance = 20

    char.player_sprite.center_x = 150
    char.player_sprite.center_y = 200
    char.player_sprite.scale = .08

    char.player_list.append(char.player_sprite)

    return char