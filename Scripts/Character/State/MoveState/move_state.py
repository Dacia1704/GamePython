from ..character_state import CharacterState
class MoveState(CharacterState):
  def enter(self):
    super().enter()
    print("Enter Move")

  def exit(self):
    super().exit()
    print("Exit Move")

  def update(self):
    super().update()