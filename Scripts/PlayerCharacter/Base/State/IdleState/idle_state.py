from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
class IdleState(CharacterState):
  def __init__(self, state_machine):
    super().__init__(state_machine)

  def enter(self):
    super().enter()
    #print("Enter Idle")

  def exit(self):
    super().exit()
    #print("Exit Idle")

  def update(self):
    super().update()
    #check state
    self.on_nomal_attack()
    self.on_fall()
    self.on_jump()
    self.on_move()
    self.on_hit()
    self.on_skill1()

    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.IDLE_SPEED_MODIFIER)
    self.move_vertical(GameConstants.BASE_JUMP_FORCE,GameConstants.ZERO_FORCE_MODIFIER)

    #animation
    self.update_sprite_animation(self.state_machine.character.idle_spritesheet[0],self.state_machine.character.idle_spritesheet[2],True)

  #check state


  #animation
  def draw(self, surface):
    super().draw(surface)

    offsetx = self.state_machine.character.idle_spritesheet[3] * self.state_machine.character.idle_spritesheet[1] 
    if self.state_machine.character.flip:
      offsetx = self.state_machine.character.idle_spritesheet[4] * self.state_machine.character.idle_spritesheet[1]
    offsety = self.state_machine.character.idle_spritesheet[5] * self.state_machine.character.idle_spritesheet[1]
    img = pygame.transform.flip(self.state_machine.character.idle_spritesheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))



    
 