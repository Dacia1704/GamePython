from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
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
    self.on_fall()
    self.on_jump()
    self.on_idle()

    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.MOVE_SPEED_MODIFIER)
    self.move_vertical(GameConstants.BASE_JUMP_FORCE,GameConstants.ZERO_FORCE_MODIFIER)

    #animation
    self.update_sprite_animation(self.state_machine.character.move_spritesheet,GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[2],True)

  # check change state

  
  # animation
  def draw(self, surface):
    img = pygame.transform.flip(self.state_machine.character.move_spritesheet[self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x, self.state_machine.character.rect.y))