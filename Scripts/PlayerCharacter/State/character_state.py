from .state import State
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
class CharacterState(State):
  def __init__(self, state_machine):
    self.state_machine = state_machine

    #animation
    self.update_animation_time = pygame.time.get_ticks()
    self.current_sprite_index = 0

  #update state function
  def enter(self):
    self.update_animation_time = pygame.time.get_ticks()
    self.current_sprite_index = 0
  def exit(self):
    pass
  def update(self):
    self.draw(self.state_machine.screen_surface)

  #check condition function
  def on_idle(self):
    pass
  def on_move(self):
    pass

  # logic state funcion
  def move_horizontal(self,base_speed,modifier):
    #print("move")
    dx = 0 
    speed = base_speed * modifier
    if GameInput.get_instance().left1:
      dx -= speed
    if GameInput.get_instance().right1:
      dx += speed

    self.state_machine.character.rect.x += dx
  
  #draw animation
  def draw(self,surface):
    pygame.draw.rect(surface,(255,0,0),self.state_machine.character.rect) # draw rectangle

  def update_sprite_animation(self,sprite_sheet,animation_cooldown,loop):
    max = len(sprite_sheet)
    if pygame.time.get_ticks() - self.update_animation_time > animation_cooldown: 
      self.current_sprite_index +=1
      self.update_animation_time = pygame.time.get_ticks()
    
    if self.current_sprite_index >= max:
      if loop:
        self.current_sprite_index = 0
      else:
        self.current_sprite_index = max-1



