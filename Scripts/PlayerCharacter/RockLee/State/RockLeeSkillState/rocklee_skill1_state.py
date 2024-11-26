from Scripts.PlayerCharacter.Base.State.SkillState.skill_state import SkillState
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
class RockLeeSkill1State(SkillState):
  def enter(self):
    super().enter()
    self.skill_collider_animations = GameConstants.ROCKLEE_SKILL1_COLLIDER_ANIMATIONS
    AudioManager.get_instance().play_sfx(self.state_machine.character.skill_1_sfx_name)
    self.update_knock_back_force_target([5,20],150)
    
  def exit(self):
    AudioManager.get_instance().stop_sfx(self.state_machine.character.skill_1_sfx_name)
    super().exit()

  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.skill1_spritesheet[0],self.state_machine.character.skill1_spritesheet[2],False)


  def skill_attack_enter(self):
    super().skill_attack_enter()
    if not self.state_machine.character.is_using_skill:
      self.state_machine.character.target.dam_take = 25
      self.state_machine.character.mana_consume = 20
      #execute attack
      self.state_machine.character.is_using_skill = True
    self.state_machine.character.mana -= self.state_machine.character.mana_consume

  # animation
  def draw(self, surface):
    super().draw(surface)
    self.draw_skill_animation(surface,self.state_machine.character.skill1_spritesheet,GameConstants.ROCKLEE_SKILL1_COLLIDER_DICTIONARY)
