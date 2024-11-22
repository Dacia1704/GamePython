from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.PlayerCharacter.RockLee.State.NomalAttackState.rocklee_nomal_attack1_state import RockLeeNomalAttack1State
from Scripts.PlayerCharacter.RockLee.State.NomalAttackState.rocklee_nomal_attack2_state import RockLeeNomalAttack2State
from Scripts.PlayerCharacter.RockLee.State.NomalAttackState.rocklee_nomal_attack3_state import RockLeeNomalAttack3State
class RockLeeStateMachine(StateMachine):
  def __init__(self,character,screen_surface):
    super().__init__(character,screen_surface)
    self.nomal_attack1 = RockLeeNomalAttack1State(self)
    self.nomal_attack2 = RockLeeNomalAttack2State(self)
    self.nomal_attack3 = RockLeeNomalAttack3State(self)