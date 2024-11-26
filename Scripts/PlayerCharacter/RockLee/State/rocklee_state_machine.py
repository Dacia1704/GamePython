from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.PlayerCharacter.RockLee.State.NomalAttackState.rocklee_nomal_attack1_state import RockLeeNomalAttack1State
from Scripts.PlayerCharacter.RockLee.State.NomalAttackState.rocklee_nomal_attack2_state import RockLeeNomalAttack2State
from Scripts.PlayerCharacter.RockLee.State.NomalAttackState.rocklee_nomal_attack3_state import RockLeeNomalAttack3State
from Scripts.PlayerCharacter.RockLee.State.RockLeeSkillState.rocklee_skill1_state import RockLeeSkill1State
from Scripts.PlayerCharacter.RockLee.State.RockLeeSkillState.rocklee_skill2_state import RockLeeSkill2State
from Scripts.PlayerCharacter.RockLee.State.RockLeeSkillState.rocklee_skill3_state import RockLeeSkill3State
class RockLeeStateMachine(StateMachine):
  def __init__(self,character,screen_surface):
    super().__init__(character,screen_surface)
    self.nomal_attack1 = RockLeeNomalAttack1State(self)
    self.nomal_attack2 = RockLeeNomalAttack2State(self)
    self.nomal_attack3 = RockLeeNomalAttack3State(self)
    self.skill1_state = RockLeeSkill1State(self)
    self.skill2_state = RockLeeSkill2State(self)
    self.skill3_state = RockLeeSkill3State(self)