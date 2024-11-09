import pygame
from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.game_constants import GameConstants
from Scripts.Input.game_input import GameInput
class Character:
  def __init__(self,x,y,screen_surface):
    self.state_machine = StateMachine(self,screen_surface) #for override
    self.rect = None   #for override
    self.health = GameConstants.BASE_HEALTH
    

    # 0: sprite_sheet, 1: image_scale, 2: animation_cooldown, 3: offset_x, 4: offset_y
    self.idle_spritesheet = None #for override
    self.move_spritesheet = None #for override
    self.jump_spritesheet = None #for override
    self.fall_spritesheet = None #for override
    self.nomal_attack1_spritesheet = None #for override
    self.nomal_attack2_spritesheet = None #for override
    self.nomal_attack3_spritesheet = None #for override

    self.is_grounded = True

    self.flip = False

    self.vel_y = 0
    self.is_jumping = False
    self.need_reset_jumpkey = False

    self.is_nomal_attacking = False

    self.is_falling = False
  def update(self):
    self.update_flip()
    self.state_machine.update()

  def start(self):
    self.state_machine.change_state(self.state_machine.idle_state)

  def handle_image(self,sprite_sheet_raw,width,height,number_of_sprite,image_scale):
    animation_list = []
    for x in range(number_of_sprite):
      temp_img = sprite_sheet_raw.subsurface(x * width,0 , width, height)
      animation_list.append(pygame.transform.scale(temp_img, (width * image_scale, height * image_scale)))
    return animation_list
  
  def update_flip(self):
    if GameInput.get_instance().left_p1:
      self.flip = True
    if GameInput.get_instance().right_p1:
      self.flip = False
    
  