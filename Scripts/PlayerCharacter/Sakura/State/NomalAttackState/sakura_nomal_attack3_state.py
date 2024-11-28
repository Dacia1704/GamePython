from Scripts.PlayerCharacter.Base.State.NomalAttackState.nomal_attack_state import NomalAttackState
import pygame
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
class SakuraNomalAttack3State(NomalAttackState):
  def enter(self):
    super().enter()
    AudioManager.get_instance().play_sfx(self.state_machine.character.nomal_attack_3_sfx_name)
    self.attack_collider_animations = GameConstants.SAKURA_ATTACK3_COLLIDER_ANIMATIONS

  def exit(self):
    super().exit()
    AudioManager.get_instance().stop_sfx(self.state_machine.character.nomal_attack_3_sfx_name)
  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.nomal_attack3_spritesheet[0],self.state_machine.character.nomal_attack3_spritesheet[2],False)
  def nomal_attack_enter(self):
    super().nomal_attack_enter()
    if not self.state_machine.character.is_nomal_attacking:
      #execute attack
      self.state_machine.character.is_nomal_attacking = True

  # animation
  def draw(self, surface):
    super().draw(surface)
    self.draw_attack_animation(surface,self.state_machine.character.nomal_attack3_spritesheet,GameConstants.SAKURA_ATTACK3_COLLIDER_DICTIONARY)