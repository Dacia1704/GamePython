
from Scripts.PlayerCharacter.Base.State.SkillState.skill_state import SkillState
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
class SakuraSkill1State(SkillState):
  def enter(self):
    super().enter()
    AudioManager.get_instance().play_sfx(self.state_machine.character.skill_1_sfx_name)
    self.skill_collider_animations = GameConstants.SAKURA_SKILL1_COLLIDER_ANIMATIONS
    self.update_knock_back_force_target(
      [GameConstants.SAKURA_SKILL_1_PROPS[2][0], GameConstants.SAKURA_SKILL_1_PROPS[2][1]],
      GameConstants.SAKURA_SKILL_1_PROPS[3])
    self.update_target_dam_take(GameConstants.SAKURA_SKILL_1_PROPS[0])

  def exit(self):
    AudioManager.get_instance().stop_sfx(self.state_machine.character.skill_1_sfx_name)
    super().exit()


  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.skill1_spritesheet[0],self.state_machine.character.skill1_spritesheet[2],False)


  def skill_attack_enter(self):
    super().skill_attack_enter()
    if not self.state_machine.character.is_using_skill:
      print("update")

      #execute attack
      self.state_machine.character.is_using_skill = True
    self.state_machine.character.health = min(self.state_machine.character.health + 10, 300)
    self.state_machine.character.mana -= self.state_machine.character.mana_consume_skill_1
  # animation
  def draw(self, surface):
    super().draw(surface)
    self.draw_skill_animation(surface,self.state_machine.character.skill1_spritesheet,GameConstants.SAKURA_SKILL1_COLLIDER_DICTIONARY)
