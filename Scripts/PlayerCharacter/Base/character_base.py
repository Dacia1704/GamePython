import pygame
from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.game_constants import GameConstants
from Scripts.Input.game_input import GameInput
from Scripts.Attackable.attackable import Attackable
from Scripts.Damable.damable import Damable
from Scripts.Audio.audio_manager import AudioManager
class Character (Attackable,Damable):
  def __init__(self,game_scene,player_id,x,y,screen_surface,target):
    Attackable.__init__(self)
    Damable.__init__(self)
    self.game_scene = game_scene
    self.state_machine = StateMachine(self,screen_surface) #for override
    self.rect = None   #for override
    self.health = GameConstants.BASE_HEALTH
    self.mana = GameConstants.BASE_MANA
    self.player_id = player_id
    self.last_dash_time = 0  # Thời gian Dash lần cuối
    self.dash_cooldown = 500  # Thời gian delay giữa các lần Dash (ms)
    
    #input
    self.right_input = False
    self.left_input = False
    self.up_input = False
    self.down_input = False
    self.nomal_attack_input = False
    self.skill_1_input = False
    self.skill_2_input = False
    self.skill_3_input = False
    self.dash_input = False
    
    # 0: sprite_sheet, 1: image_scale, 2: animation_cooldown, 3: offset_x, 4: offset_y
    self.idle_spritesheet = None #for override
    self.move_spritesheet = None #for override
    self.jump_spritesheet = None #for override
    self.fall_spritesheet = None #for override
    self.nomal_attack1_spritesheet = None #for override
    self.nomal_attack2_spritesheet = None #for override
    self.nomal_attack3_spritesheet = None #for override
    self.hit_spritesheet = None # for override
    self.skill1_spritesheet = None # for override
    self.skill2_spritesheet = None # for override
    self.skill3_spritesheet = None # for override
    self.dash_spritesheet = None  # for override
    self.death_spritesheet =None # for override
    self.is_grounded = True

    #logic
    self.flip = False

    self.vel_y = 0
    self.vel_x = 0 
    self.is_jumping = False
    self.need_reset_jumpkey = False

    self.is_nomal_attacking = False
    self.is_using_skill = False

    self.is_falling = False
    self.is_hitting = False
    self.is_running_death_animation = False
    self.is_using_skill = False
    self.is_dashing = False 

    self.mana_consume_skill_1 = 0 #For override
    self.mana_consume_skill_2 = 0 #For override
    self.mana_consume_skill_3 = 0 #For override
    #attack
    self.target = target

    #knockback
    self.is_knockbacking = False
    self.time_start_knockback = pygame.time.get_ticks()
    self.knockback_direction = [0,0]
    self.knockback_time = 100

    #sfx
    self.move_sfx_name = ""
    self.jump_sfx_name = ""
    self.hit_sfx_name = ""
    self.death_sfx_name = ""
    self.win_sfx_name = ""
    self.nomal_attack_1_sfx_name = ""
    self.nomal_attack_2_sfx_name = ""
    self.nomal_attack_3_sfx_name = ""
    self.skill_1_sfx_name = ""
    self.skill_2_sfx_name = ""
    self.skill_3_sfx_name = ""

    #heal mana by time
    self.mana_heal = 1
    self.mana_heal_cooldown = 500
    self.mana_heal_time_counter = pygame.time.get_ticks()



  def update(self):
    self.update_player_input()
    self.update_flip()
    self.state_machine.update()
    self.heal_mana_by_time()

  def start(self):
    self.state_machine.change_state(self.state_machine.idle_state)

  def handle_image(self,sprite_sheet_raw,width,height,number_of_sprite,image_scale):
    animation_list = []
    for x in range(number_of_sprite):
      temp_img = sprite_sheet_raw.subsurface(x * width,0 , width, height)
      animation_list.append(pygame.transform.scale(temp_img, (width * image_scale, height * image_scale)))
    return animation_list
  
  def update_flip(self):
    if self.left_input:
      self.flip = True
    if self.right_input:
      self.flip = False
    
  def update_player_input(self):
    if self.player_id==1:
      self.right_input = GameInput.get_instance().right_p1
      self.left_input = GameInput.get_instance().left_p1
      self.up_input = GameInput.get_instance().up_p1
      self.down_input = GameInput.get_instance().down_p1
      self.nomal_attack_input = GameInput.get_instance().nomal_attack_p1
      self.skill_1_input = GameInput.get_instance().skill_1_p1
      self.skill_2_input = GameInput.get_instance().skill_2_p1
      self.skill_3_input = GameInput.get_instance().skill_3_p1
      self.dash_input = GameInput.get_instance().dash_p1
    if self.player_id==2:
      self.right_input = GameInput.get_instance().right_p2
      self.left_input = GameInput.get_instance().left_p2
      self.up_input = GameInput.get_instance().up_p2
      self.down_input = GameInput.get_instance().down_p2
      self.nomal_attack_input = GameInput.get_instance().nomal_attack_p2
      self.skill_1_input = GameInput.get_instance().skill_1_p2
      self.skill_2_input = GameInput.get_instance().skill_2_p2
      self.skill_3_input = GameInput.get_instance().skill_3_p2
      self.dash_input = GameInput.get_instance().dash_p2

  #attackable
  def draw_attack_area_collider(self, pos_relate_centerxy, size,target):
    attacking_rect = None
    if not self.state_machine.character.flip:
      attacking_rect = pygame.Rect(self.state_machine.character.rect.centerx + pos_relate_centerxy[0], self.state_machine.character.rect.centery + pos_relate_centerxy[1], size[0], size[1])
    else:
      attacking_rect = pygame.Rect(self.state_machine.character.rect.centerx - pos_relate_centerxy[0] - size[0], self.state_machine.character.rect.centery + pos_relate_centerxy[1], size[0], size[1])
    # pygame.draw.rect(self.state_machine.screen_surface, (0,255,0),attacking_rect)

    if attacking_rect.colliderect(target.damable_rect):
      target.is_hitting = True

  #damable
  def draw_get_dam_area_collider(self, pos_relate_centerxy, size):
    if not self.state_machine.character.flip:
      self.damable_rect = pygame.Rect(self.state_machine.character.rect.centerx + pos_relate_centerxy[0], self.state_machine.character.rect.centery + pos_relate_centerxy[1], size[0], size[1])
    else:
      self.damable_rect = pygame.Rect(self.state_machine.character.rect.centerx - pos_relate_centerxy[0] - size[0], self.state_machine.character.rect.centery + pos_relate_centerxy[1], size[0], size[1])
    # pygame.draw.rect(self.state_machine.screen_surface, (255,255,255),self.damable_rect)

  #knockback
  def update_knockback(self,direction,time):
    self.knockback_direction = direction
    self.knockback_time = time

  #sfx
  def setup_sfx(self,name,path):
    AudioManager.get_instance().load_sfx(name,path)
    return name # return name về để set name cho sfx trên self

  #heal mana
  def heal_mana_by_time(self):
    if pygame.time.get_ticks() - self.mana_heal_time_counter > self.mana_heal_cooldown:
      self.mana_heal_time_counter = pygame.time.get_ticks()
      if self.mana+ self.mana_heal <= GameConstants.BASE_MANA:
        self.mana = self.mana + self.mana_heal  
      else :
        self.mana = GameConstants.BASE_MANA



