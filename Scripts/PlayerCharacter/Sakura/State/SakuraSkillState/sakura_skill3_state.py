
from Scripts.PlayerCharacter.Base.State.SkillState.skill_state import SkillState
from Scripts.game_constants import GameConstants
class SakuraSkill3State(SkillState):
  def enter(self):
    super().enter()
    self.skill_collider_animations = GameConstants.SAKURA_SKILL3_COLLIDER_ANIMATIONS
    self.update_knock_back_force_target([5,20],150)

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
    self.draw_skill_animation(surface,self.state_machine.character.skill3_spritesheet,GameConstants.SAKURA_SKILL3_COLLIDER_DICTIONARY)
