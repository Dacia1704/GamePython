from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
class JumpState(CharacterState):
  #base function
  def enter(self):
    super().enter()
    #print("Enter Jump")
    self.state_machine.character.need_reset_jumpkey = True

  def exit(self):
    super().exit()
    #print("Exit Jump")

  def update(self):
    super().update()
    #check state
    self.on_fall()
    self.on_idle()
    self.on_hit()

    self.on_dash()
    self.on_skill1()
    self.on_skill2()
    self.on_skill3()

    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.MOVE_SPEED_MODIFIER)
    self.move_vertical(GameConstants.BASE_JUMP_FORCE,GameConstants.JUMP_FORCE_MODIFIER)


    #animation
    self.update_sprite_animation(self.state_machine.character.jump_spritesheet[0],self.state_machine.character.jump_spritesheet[2],False)


  
  # animation
  def draw(self, surface):
    super().draw(surface)
    offsetx = self.state_machine.character.jump_spritesheet[3] * self.state_machine.character.jump_spritesheet[1] 
    if self.state_machine.character.flip:
      offsetx = self.state_machine.character.jump_spritesheet[4] * self.state_machine.character.jump_spritesheet[1]
    offsety = self.state_machine.character.jump_spritesheet[5] * self.state_machine.character.jump_spritesheet[1]
    img = pygame.transform.flip(self.state_machine.character.jump_spritesheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))