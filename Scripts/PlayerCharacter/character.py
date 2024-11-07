import pygame
from Scripts.PlayerCharacter.State.state_machine import StateMachine
from Scripts.game_constants import GameConstants
class Character:
  def __init__(self,x,y,screen_surface):
    self.state_machine = StateMachine(self,screen_surface)
    self.rect = pygame.Rect((x,y,80,180))
    self.idle_spritesheet = self.handle_image(pygame.image.load(GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),34,50,6,GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[1])
    self.idle_spritesheet = self.handle_image(pygame.image.load(GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),34,50,6,GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[1])

  def update(self):
    self.state_machine.update()

  def start(self):
    self.state_machine.change_state(self.state_machine.idle_state)

  def handle_image(self,sprite_sheet_raw,width,height,number_of_sprite,image_scale):
    animation_list = []
    for x in range(number_of_sprite):
      temp_img = sprite_sheet_raw.subsurface(x * width,0 , width, height)
      animation_list.append(pygame.transform.scale(temp_img, (width * image_scale, height * image_scale)))
    return animation_list
  