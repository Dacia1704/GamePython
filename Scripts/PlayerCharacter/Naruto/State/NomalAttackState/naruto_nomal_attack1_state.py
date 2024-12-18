from Scripts.PlayerCharacter.Base.State.NomalAttackState.nomal_attack_state import NomalAttackState
import pygame
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
class NarutoNomalAttack1State(NomalAttackState):

  def enter(self):
    super().enter()
    AudioManager.get_instance().play_sfx(self.state_machine.character.nomal_attack_1_sfx_name)
    self.attack_collider_animations = GameConstants.NARUTO_ATTACK1_COLLIDER_ANIMATIONS

  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.nomal_attack2_spritesheet[0],self.state_machine.character.nomal_attack1_spritesheet[2],False)

  def exit(self):
    super().exit()
    AudioManager.get_instance().stop_sfx(self.state_machine.character.nomal_attack_1_sfx_name)

  def nomal_attack_enter(self):
    super().nomal_attack_enter()
    if not self.state_machine.character.is_nomal_attacking:
      #execute attack
      self.state_machine.character.is_nomal_attacking = True

  # animation
  def draw(self, surface):
    super().draw(surface)
    self.draw_attack_animation(surface,self.state_machine.character.nomal_attack1_spritesheet,GameConstants.NARUTO_ATTACK1_COLLIDER_DICTIONARY)

