from Scripts.PlayerCharacter.Base.State.state_machine import StateMachine
from Scripts.PlayerCharacter.Naruto.State.NomalAttackState.naruto_nomal_attack_state import NarutoNomalAttackState
class NarutoStateMachine(StateMachine):
  def __init__(self,character,screen_surface):
    super().__init__(character,screen_surface)
    self.nomal_attack = NarutoNomalAttackState(self)