from Scripts.PlayerCharacter.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
class IdleState(CharacterState):
  def __init__(self, state_machine):
    super().__init__(state_machine)

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

    #animation
    self.update_sprite_animation(self.state_machine.character.idle_spritesheet,GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[2],True)


  def on_move(self):
    if GameInput.get_instance().left1 or GameInput.get_instance().right1:
      self.state_machine.change_state(self.state_machine.move_state) 

  def draw(self, surface):
    # img = pygame.transform.flip(self.animation_sprite_sheet[self.current_sprite_index], False, False)
    img = pygame.transform.flip(self.state_machine.character.idle_spritesheet[self.current_sprite_index], False, False)
    surface.blit(img, (self.state_machine.character.rect.x, self.state_machine.character.rect.y))



    
 