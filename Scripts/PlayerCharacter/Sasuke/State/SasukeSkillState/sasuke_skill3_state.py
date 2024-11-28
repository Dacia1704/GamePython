
from Scripts.PlayerCharacter.Base.State.SkillState.skill_state import SkillState
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
class SasukeSkill3State(SkillState):
  def enter(self):
    super().enter()
    self.skill_collider_animations = GameConstants.SASUKE_SKILL3_COLLIDER_ANIMATIONS
    AudioManager.get_instance().play_sfx(self.state_machine.character.skill_3_sfx_name)
    self.update_target_dam_take(GameConstants.SASUKE_SKILL_3_PROPS[0])
    self.state_machine.character.mana -= self.state_machine.character.mana_consume_skill_3
  def exit(self):
    AudioManager.get_instance().stop_sfx(self.state_machine.character.skill_3_sfx_name)
    super().exit()
  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.skill3_spritesheet[0],self.state_machine.character.skill3_spritesheet[2],False)


  def skill_attack(self):
    super().skill_attack()
    if not self.state_machine.character.is_using_skill:
      #execute attack
      self.state_machine.character.is_using_skill = True
    

  # animation
  def draw(self, surface):
    super().draw(surface)
    self.draw_skill_animation(surface,self.state_machine.character.skill3_spritesheet,GameConstants.SASUKE_SKILL3_COLLIDER_DICTIONARY)