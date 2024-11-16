from Scripts.PlayerCharacter.Base.State.NomalAttackState.nomal_attack_state import NomalAttackState
import pygame
from Scripts.game_constants import GameConstants
class NarutoNomalAttack3State(NomalAttackState):
  def enter(self):
    super().enter()
    self.attack_collider_animations = GameConstants.NARUTO_ATTACK3_COLLIDER_ANIMATIONS
  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.nomal_attack3_spritesheet[0],self.state_machine.character.nomal_attack3_spritesheet[2],False)
  def nomal_attack(self):
    super().nomal_attack()
    if not self.state_machine.character.is_nomal_attacking:
      #execute attack
      self.state_machine.character.is_nomal_attacking = True

  # animation
  def draw(self, surface):
    super().draw(surface)
    self.draw_attack_animation(surface,self.state_machine.character.nomal_attack3_spritesheet,GameConstants.NARUTO_ATTACK3_COLLIDER_DICTIONARY)

