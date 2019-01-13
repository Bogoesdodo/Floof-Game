import arcade
import Character
all_sprite_list = None
all_sprite_list = arcade.SpriteList()

class npc:
    npc_list = None
    npc_sprite = None
    #npc_sprite_front = None
    #npc_sprite_back = None
    #npc_sprite_right = None
    #npc_sprite_left = None
    physics_engine = None
    name = None
    say = ""
    interact = False

    def __init__(self, name):
        self.name = name
        self.npc_list = None
        self.npc_sprite = None
        self.physics_engine = None

    #def interaction (self,  ):
     #   self.interact =


def setup_npc0():
    size = .5
    boy = npc("Steven")
    boy.npc_list = arcade.SpriteList()
    boy.npc_sprite = arcade.AnimatedWalkingSprite()#("npc1.png",0.5)

    boy.npc_sprite.stand_right_textures = []
    boy.npc_sprite.stand_right_textures.append(arcade.load_texture("npc1.png", scale = size))

    boy.npc_sprite.stand_left_textures = []
    boy.npc_sprite.stand_left_textures.append(arcade.load_texture("wall.png", scale = size))

    boy.npc_sprite.walk_right_textures = []
    boy.npc_sprite.walk_right_textures.append(arcade.load_texture("npc1.png", scale = size * 5))
    boy.npc_sprite.walk_right_textures.append(arcade.load_texture("npc1.png", scale = size * 5))
    boy.npc_sprite.walk_right_textures.append(arcade.load_texture("npc1.png", scale = size * 5))
    boy.npc_sprite.walk_right_textures.append(arcade.load_texture("npc1.png", scale = size * 5))

    boy.npc_sprite.walk_left_textures = []
    boy.npc_sprite.walk_left_textures.append(arcade.load_texture("hero.png", scale = size))
    boy.npc_sprite.walk_left_textures.append(arcade.load_texture("npc1.png", scale = size))
    boy.npc_sprite.walk_left_textures.append(arcade.load_texture("hero.png", scale = size))
    boy.npc_sprite.walk_left_textures.append(arcade.load_texture("hero.png", scale = size))

    boy.npc_sprite.walk_up_textures = []
    boy.npc_sprite.walk_up_textures.append(arcade.load_texture("hero.png", scale=size))
    boy.npc_sprite.walk_up_textures.append(arcade.load_texture("hero.png", scale=size))
    boy.npc_sprite.walk_up_textures.append(arcade.load_texture("hero.png", scale=size))
    boy.npc_sprite.walk_up_textures.append(arcade.load_texture("hero.png", scale=size))

    boy.npc_sprite.walk_down_textures = []
    boy.npc_sprite.walk_down_textures.append(arcade.load_texture("hero.png", scale=size))
    boy.npc_sprite.walk_down_textures.append(arcade.load_texture("hero.png", scale=size))
    boy.npc_sprite.walk_down_textures.append(arcade.load_texture("hero.png", scale=size))
    boy.npc_sprite.walk_down_textures.append(arcade.load_texture("hero.png", scale=size))


    boy.npc_sprite.texture_change_distance = 20

    boy.npc_sprite.center_x = 150
    boy.npc_sprite.center_y = 200
    boy.npc_sprite.scale = .08

    boy.npc_list.append(boy.npc_sprite)
    all_sprite_list.append(boy.npc_sprite)
    return boy



