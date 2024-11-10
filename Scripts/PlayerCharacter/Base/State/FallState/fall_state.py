from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
class FallState(CharacterState):
  #base function
  def enter(self):
    super().enter()
    #print("Enter Fall")

  def exit(self):
    super().exit()
    #print("Exit Fall")

  def update(self):
    super().update()
    #check state
    self.on_move()
    self.on_idle()


    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.MOVE_SPEED_MODIFIER)
    self.move_vertical(GameConstants.BASE_JUMP_FORCE,GameConstants.ZERO_FORCE_MODIFIER)


    #animation
    self.update_sprite_animation(self.state_machine.character.fall_spritesheet[0],self.state_machine.character.fall_spritesheet[2],False)


  
  # animation
  def draw(self, surface):
    offsetx = self.state_machine.character.fall_spritesheet[3] * self.state_machine.character.fall_spritesheet[1]
    offsety = self.state_machine.character.fall_spritesheet[4] * self.state_machine.character.fall_spritesheet[1]
    img = pygame.transform.flip(self.state_machine.character.fall_spritesheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))

  #checkstate
  def on_idle(self):
    if not self.state_machine.character.left_input  and not self.state_machine.character.right_input and (not self.state_machine.character.up_input or (self.state_machine.character.up_input and self.state_machine.character.need_reset_jumpkey)) and not self.state_machine.character.down_input and self.state_machine.character.is_grounded:
      self.state_machine.change_state(self.state_machine.idle_state) 