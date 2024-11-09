from .state import State
from .IdleState.idle_state import IdleState
from .MoveState.move_state import MoveState
from .JumpState.jump_state import JumpState
from .FallState.fall_state import FallState
from .NomalAttackState.nomal_attack_state import NomalAttackState
class StateMachine:
  def __init__(self,character,screen_surface):
    self.character = character
    self.idle_state = IdleState(self)
    self.move_state = MoveState(self)
    self.jump_state = JumpState(self)
    self.fall_state = FallState(self)
    self.nomal_attack1 = NomalAttackState(self)
    self.nomal_attack2 = NomalAttackState(self)
    self.nomal_attack3 = NomalAttackState(self)
    self.current_state = None
    self.screen_surface = screen_surface
    
  def change_state(self,new_state: State):
    if self.current_state != None:
      self.current_state.exit()
    self.current_state = new_state
    self.current_state.enter()
  def update(self):
    self.current_state.update()