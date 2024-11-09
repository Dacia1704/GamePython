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
    #print("Exit Move")

  def update(self):
    super().update()
    #check state
    self.on_nomal_attack()
    self.on_fall()
    self.on_jump()
    self.on_idle()

    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.MOVE_SPEED_MODIFIER)
    self.move_vertical(GameConstants.BASE_JUMP_FORCE,GameConstants.ZERO_FORCE_MODIFIER)

    #animation
    self.update_sprite_animation(self.state_machine.character.move_spritesheet[0],self.state_machine.character.move_spritesheet[2],True)

  # check change state

  
  # animation
  def draw(self, surface):
    offsetx = self.state_machine.character.move_spritesheet[3] * self.state_machine.character.move_spritesheet[1]
    offsety = self.state_machine.character.move_spritesheet[4] * self.state_machine.character.move_spritesheet[1]
    img = pygame.transform.flip(self.state_machine.character.move_spritesheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))