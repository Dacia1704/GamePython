from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.PlayerCharacter.Sasuke.State.NomalAttackState.sasuke_nomal_attack1_state import SasukeNomalAttack1State 
from Scripts.PlayerCharacter.Sasuke.State.NomalAttackState.sasuke_nomal_attack2_state import SasukeNomalAttack2State 
from Scripts.PlayerCharacter.Sasuke.State.NomalAttackState.sasuke_nomal_attack3_state import SasukeNomalAttack3State 
class SasukeStateMachine(StateMachine):
  def __init__(self,character,screen_surface):
    super().__init__(character,screen_surface)
    self.nomal_attack1 = SasukeNomalAttack1State(self)
    self.nomal_attack2 = SasukeNomalAttack2State(self)
    self.nomal_attack3 = SasukeNomalAttack3State(self)