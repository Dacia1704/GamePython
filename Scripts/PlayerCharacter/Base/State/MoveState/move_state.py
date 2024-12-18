from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
import pygame
class MoveState(CharacterState):
  #base function
  def enter(self):
    super().enter()
    #print("Enter Move")
    AudioManager.get_instance().play_sfx(self.state_machine.character.move_sfx_name,-1)

  def exit(self):
    super().exit()
    #print("Exit Move")
    AudioManager.get_instance().stop_sfx(self.state_machine.character.move_sfx_name)

  def update(self):
    super().update()
    #check state
    self.on_nomal_attack()
    self.on_fall()
    self.on_jump()
    self.on_idle()
    self.on_hit()

    self.on_dash()
    self.on_skill1()
    self.on_skill2()
    self.on_skill3()
    #logic
    self.move_horizontal(GameConstants.BASE_SPEED,GameConstants.MOVE_SPEED_MODIFIER)
    self.move_vertical(GameConstants.BASE_JUMP_FORCE,GameConstants.ZERO_FORCE_MODIFIER)

    #animation
    self.update_sprite_animation(self.state_machine.character.move_spritesheet[0],self.state_machine.character.move_spritesheet[2],True)

  # check change state

  
  # animation
  def draw(self, surface):
    super().draw(surface)
    offsetx = self.state_machine.character.move_spritesheet[3] * self.state_machine.character.move_spritesheet[1] 
    if self.state_machine.character.flip:
      offsetx = self.state_machine.character.move_spritesheet[4] * self.state_machine.character.move_spritesheet[1]
    offsety = self.state_machine.character.move_spritesheet[5] * self.state_machine.character.move_spritesheet[1]
    img = pygame.transform.flip(self.state_machine.character.move_spritesheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))