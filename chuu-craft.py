#Dev: Pingo
#12 - 6 - 2024
#Follow on tiktok :D / chuus.fav.developer
#Im aware that this code is bad, stop bugging me >:(
#I cant force you but please give credit :D
from ursina import *
from ursina.text import Text
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina(borderless=False)
window.title = "Chuu Craft"
window.exit_button.enabled = True
player = FirstPersonController()
shimmy = 15 #dont mind the random variable names
class MyButton(Button):
    def __init__(self, text='Button', **kwargs):
        super().__init__(
            text=text,
            color=color.gray,
            highlight_color=color.white,
            pressed_color=color.lime,
            **kwargs
        )

    def on_click(self):
        exit()

grass_texture = load_texture("Assets/Textures/Grass_Block.png")
stone_texture = load_texture("Assets/Textures/Stone_Block.png")
brick_texture = load_texture("Assets/Textures/Brick_Block.png")
dirt_texture = load_texture("Assets/Textures/Dirt_Block.png")
wood_texture = load_texture("Assets/Textures/Wood_Block.png")
sky_texture = load_texture("Assets/Textures/Skybox.png")
chuu_texture = load_texture("Assets/Textures/Chuu_Block.png")
arm_texture = load_texture("Assets/Textures/Arm_Texture.png")
punch_sound = Audio("Assets/SFX/Punch_Sound.wav", loop=False, autoplay=False)
bg_music = Audio("Assets/SFX/bgmusic.wav", loop=True, autoplay=True, volume=1)
window.exit_button.visible = False
block_pick = 1
bg_music.play()
currentblock = "Grass"
pause_panel = Panel(color=color.color(0, 0, 0, 0.5), scale=window.size, enabled=False)
pause_text = Text(text="Paused", scale=3, origin=(0, -5), background_color=color.black)
credit_text = Text(text="Credits to chuus.fav.developer on tiktok", scale=1.5, origin=(0, -7.5), background_color=color.black)
credit_text.enabled = False
pause_text.enabled = False
block_text = Text(text=currentblock, scale=2, origin=(2.4,-9))
block_text.enabled = False

title_panel = Panel(scale=window.size, enabled=True, color = (1, 1, 1, 1.0))
title_text = Text(text="Chuu Craft", scale=4, origin=(0, -3), color=(0,0,0,1))
follow_text = Text(text="Follow us on TikTok: chuus.fav.developer", scale=1.5, origin=(0, -2.5), color=(0,0,0,1))
start_text = Text(text="Press SPACE to Start", scale=2, origin=(0, 1), color=(0,0,0,1))

# Title Screen
def toggle_title_screen():
    title_panel.enabled = not title_panel.enabled
    title_text.enabled = not title_text.enabled
    follow_text.enabled = not follow_text.enabled
    start_text.enabled = not start_text.enabled

# Pause Screen
def toggle_pause_menu():
    if title_panel.enabled:
        print("")
    else:
        pause_panel.enabled = not pause_panel.enabled
        pause_text.enabled = not pause_text.enabled
        credit_text.enabled = not credit_text.enabled
        player.enabled = not player.enabled

def input(key):
    if key == 'escape':
        toggle_pause_menu()
    elif key == 'space' and title_panel.enabled:
        toggle_title_screen()
        block_text.enabled = True

def update():
    global block_pick
    
    if held_keys["left mouse"] or held_keys["right mouse"]:
        hand.active()
    else:
        hand.passive()

    if held_keys["1"]: block_pick = 1
    if held_keys["2"]: block_pick = 2
    if held_keys["3"]: block_pick = 3
    if held_keys["4"]: block_pick = 4
    if held_keys["5"]: block_pick = 5
    if held_keys["6"]: block_pick = 6
    if held_keys["`"]: exit()
    
    if block_pick == 1: 
        blockpicked = "Wood_Block.png"
        currentblock = "Wood"
        block_text.text = currentblock
        block_text.origin = (5.2,-9)
    if block_pick == 2: 
        blockpicked = "Brick_Block.png"
        currentblock = "Brick"
        block_text.origin = (6.3,-9)
        block_text.text = currentblock
    if block_pick == 3: 
        blockpicked = "Chuu_Block.png"
        currentblock = "Chuu Block"
        block_text.origin = (2.5,-9)
        block_text.text = currentblock
    if block_pick == 4: 
        blockpicked = "Stone_Block.png"
        currentblock = "Stone"
        block_text.origin = (5.4,-9)
        block_text.text = currentblock
    if block_pick == 5: 
        blockpicked = "Dirt_Block.png"
        currentblock = "Dirt"
        block_text.origin = (8.4,-9)
        block_text.text = currentblock
    if block_pick == 6: 
        blockpicked = "Grass_Block.png"
        currentblock = "Grass"
        block_text.text = currentblock
        block_text.origin = (5.4,-9)

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model="Assets/Models/Block",
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.white,
            scale = 0.5
        )

    def input(self, key):
        if not pause_panel.enabled:
            if not title_panel.enabled:  # Check if game is not paused
                if self.hovered:
                    if key == "right mouse down":
                        punch_sound.play()
                        if block_pick == 1:
                            voxel = Voxel(position=self.position + mouse.normal, texture=wood_texture)
                        if block_pick == 2:
                          voxel = Voxel(position=self.position + mouse.normal, texture=brick_texture)
                        if block_pick == 3:
                            voxel = Voxel(position=self.position + mouse.normal, texture=chuu_texture)
                        if block_pick == 4:
                          voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                        if block_pick == 5:
                            voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                        if block_pick == 6:
                            voxel = Voxel(position=self.position + mouse.normal, texture=grass_texture)

                    if key == "left mouse down":
                        punch_sound.play()
                        destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model="cube",
            texture=sky_texture,
            scale=(shimmy, 15, shimmy),
            double_sided=True,
            position=(7, 7, 7)
        )

# Arm
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model="Assets/Models/Arm",
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -10, 100),
            position=Vec2(0.4, -0.8) # Adjusted position
        )
    
    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)

class MyFirstPersonController(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.speed_multiplier = 1

    def update(self):
        super().update()
        map_size = shimmy-1
        if self.x < 0: self.x = 0
        if self.x > map_size: self.x = map_size
        if self.y < 0: self.y = 0
        if self.y > map_size: self.y = map_size
        if self.z < 0: self.z = 0
        if self.z > map_size: self.z = map_size

        if held_keys['shift']:
            self.speed_multiplier = 1.4
        else:
            self.speed_multiplier = 1

        self.speed = 5 * self.speed_multiplier

player = MyFirstPersonController()
sky = Sky()
hand = Hand()

for y in range(4):
    for x in range(shimmy):
        for z in range(shimmy):
            if y == 0:
                voxel = Voxel(position=(x, y, z), texture=chuu_texture)
            elif y == 1:
                voxel = Voxel(position=(x, y, z), texture=stone_texture)
            elif y == 2:
                voxel = Voxel(position=(x, y, z), texture=dirt_texture)
            elif y == 3:
                voxel = Voxel(position=(x, y, z), texture=grass_texture)

app.run()