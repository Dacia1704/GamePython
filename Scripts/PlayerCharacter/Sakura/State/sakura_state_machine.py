from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.PlayerCharacter.Sakura.State.NomalAttackState.sakura_nomal_attack1_state import SakuraNomalAttack1State
from Scripts.PlayerCharacter.Sakura.State.NomalAttackState.sakura_nomal_attack2_state import SakuraNomalAttack2State
from Scripts.PlayerCharacter.Sakura.State.NomalAttackState.sakura_nomal_attack3_state import SakuraNomalAttack3State
from Scripts.PlayerCharacter.Sakura.State.SakuraSkillState.sakura_skill1_state import SakuraSkill1State
from Scripts.PlayerCharacter.Sakura.State.SakuraSkillState.sakura_skill2_state import SakuraSkill2State
from Scripts.PlayerCharacter.Sakura.State.SakuraSkillState.sakura_skill3_state import SakuraSkill3State
class SakuraStateMachine(StateMachine):
  def __init__(self,character,screen_surface):
    super().__init__(character,screen_surface)
    self.nomal_attack1 = SakuraNomalAttack1State(self)
    self.nomal_attack2 = SakuraNomalAttack2State(self)
    self.nomal_attack3 = SakuraNomalAttack3State(self)
    self.skill1_state = SakuraSkill1State(self)
    self.skill2_state = SakuraSkill2State(self)
    self.skill3_state = SakuraSkill3State(self)