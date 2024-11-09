from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.PlayerCharacter.Naruto.State.NomalAttackState.naruto_nomal_attack1_state import NarutoNomalAttack1State
from Scripts.PlayerCharacter.Naruto.State.NomalAttackState.naruto_nomal_attack2_state import NarutoNomalAttack2State
from Scripts.PlayerCharacter.Naruto.State.NomalAttackState.naruto_nomal_attack3_state import NarutoNomalAttack3State
class NarutoStateMachine(StateMachine):
  def __init__(self,character,screen_surface):
    super().__init__(character,screen_surface)
    self.nomal_attack1 = NarutoNomalAttack1State(self)
    self.nomal_attack2 = NarutoNomalAttack2State(self)
    self.nomal_attack3 = NarutoNomalAttack3State(self)