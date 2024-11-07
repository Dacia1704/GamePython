from .state import State
from .IdleState.idle_state import IdleState
from .MoveState.move_state import MoveState
class StateMachine:
  def __init__(self,character,screen_surface):
    self.character = character
    self.idle_state = IdleState(self)
    self.move_state = MoveState(self)
    self.current_state = None
    self.screen_surface = screen_surface
    
  def change_state(self,new_state: State):
    if self.current_state != None:
      self.current_state.exit()
    self.current_state = new_state
    self.current_state.enter()
  def update(self):
    self.current_state.update()