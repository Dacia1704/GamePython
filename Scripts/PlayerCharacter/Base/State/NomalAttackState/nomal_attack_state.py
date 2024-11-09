from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
import random
from Scripts.PlayerCharacter.Base.Attackable.attackable import Attackable
class NomalAttackState(CharacterState,Attackable):
  def __init__(self, state_machine):
    super().__init__(state_machine)


  #base function
  def enter(self):
    super().enter()
    print("Enter Nomal Attack")

  def exit(self):
    super().exit()
    #print("Exit Nomal Attack")

  def update(self):
    super().update()
    #check state
    if not self.state_machine.character.is_nomal_attacking:
      self.on_jump()
      self.on_move()
      self.on_idle()

    #logic
    self.nomal_attack()

  def nomal_attack(self):
    pass

  #attackable


