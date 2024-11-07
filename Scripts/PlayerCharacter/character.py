import pygame
from Scripts.PlayerCharacter.State.state_machine import StateMachine
class Character:
  def __init__(self,x,y,screen_surface):
    self.state_machine = StateMachine(self)
    self.rect = pygame.Rect((x,y,80,180))
    self.screen_surface = screen_surface

  def update(self):
    self.state_machine.update()
    self.draw(self.screen_surface)

  def start(self):
    self.state_machine.change_state(self.state_machine.idle_state)
    
  def draw(self,surface):
    pygame.draw.rect(surface,(255,0,0),self.rect)
  