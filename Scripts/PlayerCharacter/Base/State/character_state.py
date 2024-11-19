from .state import State
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
import random
class CharacterState(State):
  def __init__(self, state_machine ):
    self.state_machine = state_machine

    #animation
    self.update_animation_time = pygame.time.get_ticks()
    self.current_sprite_index = 0

    self.is_show_last_frame = False
    self.is_last_frame_animation_cooldown_finished = False




  #update state function
  def enter(self):
    self.update_animation_time = pygame.time.get_ticks()
    self.current_sprite_index = 0
    self.is_last_frame_animation_cooldown_finished = False
  def exit(self):
    pass
  def update(self):
    #need reset jumpkey
    if self.state_machine.character.need_reset_jumpkey and not self.state_machine.character.up_input and not self.state_machine.character.is_jumping and not self.state_machine.character.is_falling:
       self.state_machine.character.need_reset_jumpkey = False

    self.update_ground_check()
    self.draw(self.state_machine.screen_surface)


  # logic state funcion
  def move_horizontal(self,base_speed,modifier):
    dx = 0 
    speed = base_speed * modifier
    if self.state_machine.character.left_input:
      dx -= speed
    if self.state_machine.character.right_input:
      dx += speed

    #ensure player in screen
    if self.state_machine.character.rect.left + dx < 0:
      dx = -self.state_machine.character.rect.left
    if self.state_machine.character.rect.right + dx > GameConstants.SCREEN_WIDTH:
      dx = GameConstants.SCREEN_WIDTH - self.state_machine.character.rect.right
    self.state_machine.character.rect.x += dx
  
  def move_vertical(self,base_force,modifier):
    dy = 0
    #move up
    jump_force =  base_force * modifier
    if self.state_machine.character.up_input and not self.state_machine.character.is_jumping and not self.state_machine.character.is_falling:
      self.state_machine.character.vel_y = -jump_force
      self.state_machine.character.is_jumping = True

    #apply gravity
    self.state_machine.character.vel_y += GameConstants.GRAVITY
    dy += self.state_machine.character.vel_y

    if dy > 0 and self.state_machine.character.is_jumping:
      self.state_machine.character.is_falling = True
      self.state_machine.character.is_jumping = False

    #ensure player in screen
    if self.state_machine.character.rect.bottom + dy > GameConstants.SCREEN_HEIGHT - GameConstants.GROUND_Y:
      self.state_machine.character.vel_y=0
      self.state_machine.character.is_jumping = False
      self.state_machine.character.is_falling = False
      dy = GameConstants.SCREEN_HEIGHT - GameConstants.GROUND_Y - self.state_machine.character.rect.bottom
    self.state_machine.character.rect.y += dy

  def update_ground_check(self):
    if self.state_machine.character.rect.bottom >= GameConstants.SCREEN_HEIGHT - GameConstants.GROUND_Y -5:
      self.state_machine.character.is_grounded = True
    else:
      self.state_machine.character.is_grounded = False

  #knock back
  def start_knockback(self):
    self.state_machine.character.is_knockbacking = True
    self.state_machine.character.time_start_knockback = pygame.time.get_ticks()
  def knockback(self):
    if self.state_machine.character.is_knockbacking:
      if pygame.time.get_ticks() - self.state_machine.character.time_start_knockback < self.state_machine.character.knockback_time:
        dx = 0 
        horizontal_force = self.state_machine.character.knockback_direction[0]
        dx += horizontal_force
        #ensure player in screen
        if self.state_machine.character.rect.left + dx < 0:
          dx = -self.state_machine.character.rect.left
        if self.state_machine.character.rect.right + dx > GameConstants.SCREEN_WIDTH:
          dx = GameConstants.SCREEN_WIDTH - self.state_machine.character.rect.right
        
        self.state_machine.character.rect.x += dx

        dy = 0
        #move up
        vertical_force =  self.state_machine.character.knockback_direction[1]
        self.state_machine.character.vel_y = -vertical_force
        #apply gravity
        self.state_machine.character.vel_y += GameConstants.GRAVITY
        dy += self.state_machine.character.vel_y
        if dy > 0:
          self.state_machine.character.is_falling = True
        #ensure player in screen
        if self.state_machine.character.rect.bottom + dy > GameConstants.SCREEN_HEIGHT - GameConstants.GROUND_Y:
          self.state_machine.character.vel_y=0
          self.state_machine.character.is_falling = False
          dy = GameConstants.SCREEN_HEIGHT - GameConstants.GROUND_Y - self.state_machine.character.rect.bottom
        self.state_machine.character.rect.y += dy
      else:
        self.state_machine.character.is_knockbacking = False


  
  #draw animation
  def draw(self,surface):
    #pygame.draw.rect(surface,(255,0,0),self.state_machine.character.rect) # draw rectangle
    self.state_machine.character.draw_get_dam_area_collider([-self.state_machine.character.rect.width/2,-self.state_machine.character.rect.height/2],[self.state_machine.character.rect.width,self.state_machine.character.rect.height])


  def update_sprite_animation(self,sprite_sheet,animation_cooldown,loop):
    max = len(sprite_sheet)
    if pygame.time.get_ticks() - self.update_animation_time > animation_cooldown: 
      self.current_sprite_index +=1

      self.update_animation_time = pygame.time.get_ticks()
      if self.is_show_last_frame:
        self.is_last_frame_animation_cooldown_finished = True
    
    if self.current_sprite_index >= max:
      if loop:
        self.current_sprite_index = 0
      else:
        self.current_sprite_index = max-1
    

  #check change state
  def on_idle(self):
    if not self.state_machine.character.left_input  and not self.state_machine.character.right_input and not self.state_machine.character.up_input and not self.state_machine.character.down_input and self.state_machine.character.is_grounded:
      self.state_machine.change_state(self.state_machine.idle_state) 
  def on_jump(self):
    if self.state_machine.character.up_input and not self.state_machine.character.need_reset_jumpkey:
      self.state_machine.change_state(self.state_machine.jump_state) 
  def on_move(self):
    if (self.state_machine.character.left_input or self.state_machine.character.right_input) and self.state_machine.character.is_grounded :
      self.state_machine.change_state(self.state_machine.move_state) 
  def on_fall(self):
    if not self.state_machine.character.is_jumping and not self.state_machine.character.is_grounded :
      self.state_machine.change_state(self.state_machine.fall_state)
  def on_nomal_attack(self):
    random_attack =  random.randint(1, 3)
    #random_attack = 1   # test
    if self.state_machine.character.nomal_attack_input and self.state_machine.character.is_grounded:
      if random_attack ==1:
        self.state_machine.change_state(self.state_machine.nomal_attack1)   
        self.state_machine.character.target.update_knockback([15,5],150)
      elif random_attack ==2:
        self.state_machine.change_state(self.state_machine.nomal_attack2)
        self.state_machine.character.target.update_knockback([15,5],150)
      elif random_attack ==3:
        self.state_machine.change_state(self.state_machine.nomal_attack3)
        self.state_machine.character.target.update_knockback([15,5],150)

  def on_hit(self):
    if self.state_machine.character.is_hitting: 
      self.state_machine.change_state(self.state_machine.hit_state)
      
  def on_skill1(self):
    if self.state_machine.character.skill_1_input and self.state_machine.character.is_grounded:
      self.state_machine.change_state(self.state_machine.skill1_state) 
      self.state_machine.character.target.update_knockback([5,20],150)
