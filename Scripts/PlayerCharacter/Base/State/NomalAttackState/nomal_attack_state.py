from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
class NomalAttackState(CharacterState):
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

    #animation
    self.update_sprite_animation(self.state_machine.character.nomal_attack_spritesheet[0],GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[2],False)

  # check change state


  def nomal_attack(self):
    pass