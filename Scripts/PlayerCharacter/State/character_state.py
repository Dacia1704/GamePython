from .state import State
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
class CharacterState(State):
  def __init__(self, state_machine):
    self.state_machine = state_machine

  #update state function
  def enter(self):
    pass
  def exit(self):
    pass
  def update(self):
    pass

  #check condition function
  def on_idle(self):
    pass
  def on_move(self):
    pass

  # logic state funcion
  def move_horizontal(self,base_speed,modifier):
    #print("move")
    dx = 0 
    speed = base_speed * modifier
    if GameInput.get_instance().left1:
      dx -= speed
    if GameInput.get_instance().right1:
      dx += speed
    print(speed,dx)

    self.state_machine.character.rect.x += dx
