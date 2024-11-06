from ..character_state import CharacterState
class IdleState(CharacterState):
  def enter(self):
    super().enter()
    print("Enter Idle")

  def exit(self):
    super().exit()
    print("Exit Idle")

  def update(self):
    super().update()