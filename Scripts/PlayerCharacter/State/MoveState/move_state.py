from Scripts.PlayerCharacter.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
class MoveState(CharacterState):
  #base function
  def enter(self):
    super().enter()
    print("Enter Move")

  def exit(self):
    super().exit()
    print("Exit Move")

  def update(self):
    super().update()
    #check state
    self.on_idle()

    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.MOVE_SPEED_MODIFIER)

  # check change state
  def on_idle(self):
    if not GameInput.get_instance().left1  and not GameInput.get_instance().right1 and not GameInput.get_instance().up1 and not GameInput.get_instance().down1:
      self.state_machine.change_state(self.state_machine.idle_state) 