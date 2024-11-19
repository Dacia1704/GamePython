from Scripts.PlayerCharacter.Base.State.SkillState.skill_state import SkillState
from Scripts.game_constants import GameConstants
class NarutoSkill1State(SkillState):
  def enter(self):
    super().enter()
    self.skill_collider_animations = GameConstants.NARUTO_SKILL1_COLLIDER_ANIMATIONS

  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.skill1_spritesheet[0],self.state_machine.character.skill1_spritesheet[2],False)


  def skill_attack(self):
    super().skill_attack()
    if not self.state_machine.character.is_using_skill:
      #execute attack
      self.state_machine.character.is_using_skill = True

  # animation
  def draw(self, surface):
    super().draw(surface)
    self.draw_skill_animation(surface,self.state_machine.character.skill1_spritesheet,GameConstants.NARUTO_SKILL1_COLLIDER_DICTIONARY)