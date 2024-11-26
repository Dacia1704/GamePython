from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.PlayerCharacter.Sasuke.State.NomalAttackState.sasuke_nomal_attack1_state import SasukeNomalAttack1State 
from Scripts.PlayerCharacter.Sasuke.State.NomalAttackState.sasuke_nomal_attack2_state import SasukeNomalAttack2State 
from Scripts.PlayerCharacter.Sasuke.State.NomalAttackState.sasuke_nomal_attack3_state import SasukeNomalAttack3State 
from Scripts.PlayerCharacter.Sasuke.State.SasukeSkillState.sasuke_skill1_state import SasukeSkill1State
from Scripts.PlayerCharacter.Sasuke.State.SasukeSkillState.sasuke_skill2_state import SasukeSkill2State
from Scripts.PlayerCharacter.Sasuke.State.SasukeSkillState.sasuke_skill3_state import SasukeSkill3State
class SasukeStateMachine(StateMachine):
  def __init__(self,character,screen_surface):
    super().__init__(character,screen_surface)
    self.nomal_attack1 = SasukeNomalAttack1State(self)
    self.nomal_attack2 = SasukeNomalAttack2State(self)
    self.nomal_attack3 = SasukeNomalAttack3State(self)
    self.skill1_state = SasukeSkill1State(self)
    self.skill2_state = SasukeSkill2State(self)
    self.skill3_state = SasukeSkill3State(self)