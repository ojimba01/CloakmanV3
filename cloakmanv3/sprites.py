
from blocks import *
from config import *
animation_frames = {}

class sprites():
    def __init__(self):
        pass
    def load_animation(path,frame_durations):
        global animation_frames
        animation_name = path.split('/')[-1]
        animation_frame_data = []
        n = 0
        for frame in frame_durations:
            animation_frame_id = animation_name + '_' + str(n)
            img_loc = path + '/' + animation_frame_id + '.png'
            animation_image = blocks.transformsprites(img_loc).convert()
            animation_image.set_colorkey((255,255,255))
            animation_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frame_data.append(animation_frame_id)
            n += 1
        return animation_frame_data
    def change_action(action_var,frame,new_value):
        if action_var != new_value:
            action_var = new_value
            frame = 0
        return action_var,frame

class animations():
    def __init__(self):
        self.animation_database = {}
        self.animation_database['run'] = sprites.load_animation('player_animations/run',[7,7,7,7,7,7])
        self.animation_database['idle'] = sprites.load_animation('player_animations/idle',[7,7,7,7])
        self.animation_database['jump'] = sprites.load_animation('player_animations/jump',[4,4,4])
        self.animation_database['jumpdown'] = sprites.load_animation('player_animations/jumpdown',[4,4,4])


#-----------------------------------------------------------------------------------------------------------------------
# Potentially useful attributes:
# self.moving_right = False
# self.moving_left = False
# self.jumping = False
# self.falling = False
# self.vertical_momentum = 0
# self.air_timer=0
# self.player_action = 'idle'
# self.player_frame = 0
# self.player_flip = False
# self.player_rect = pygame.Rect(player_rect)
# self.player_image = pygame.image.load('spritesheets/player/player.png')
# self.player_image.set_colorkey((255,255,255))
# self.player_image_flip = pygame.transform.flip(self.player_image,True,False)
# self.player_image_flip.set_colorkey((255,255,255))
# self.player_image_flip.set_alpha(100)
# self.player_image.set_alpha(100)
# self.player_image_flip.convert()
# self.player_image.convert()
# self.player_image_flip.set_alpha(100)
# self.player_image.set_alpha(100)
# self.player_image_flip.convert()
# self.player_image.convert()
# self.player_image_flip.set_alpha(100)
# self.player_image.set_alpha(100)
# self.player_image_flip.convert()
# self.player_image.convert()
# self.player_image_flip.set_alpha(100)
# self.player_image.set_alpha(100)
# self.player_image_flip.convert()
# self.player_image.convert()
# self.player_image_flip.set_alpha(100)
# self.player_image.set_alpha(100)
# self.player_image_flip.convert()
# self.player_image.convert()
# self.player_image_flip.set_alpha(100)