from Scripts.PlayerCharacter.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
class IdleState(CharacterState):
  def enter(self):
    super().enter()
    print("Enter Idle")

  def exit(self):
    super().exit()
    print("Exit Idle")

  def update(self):
    super().update()
    #check state
    self.on_move()

    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.IDLE_SPEED_MODIFIER)


  def on_move(self):
    if GameInput.get_instance().left1 or GameInput.get_instance().right1:
      self.state_machine.change_state(self.state_machine.move_state) 


    
 