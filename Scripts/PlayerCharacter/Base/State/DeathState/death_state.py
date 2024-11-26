from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
import pygame
class DeathState(CharacterState):
  def __init__(self, state_machine):
    super().__init__(state_machine)

  def enter(self):
    super().enter()
    #print("Enter hit")
    AudioManager.get_instance().play_sfx(self.state_machine.character.hit_sfx_name)
    self.state_machine.character.health =0
    self.start_knockback()

  def exit(self):
    super().exit()
    AudioManager.get_instance().stop_sfx(self.state_machine.character.hit_sfx_name)
    self.state_machine.character.reset_damable()

  def update(self):
    super().update()
    if not self.state_machine.character.is_running_death_animation and not self.state_machine.character.is_knockbacking:
      self.state_machine.character.game_scene.battle_finish = True

      
    #logic
    self.knockback()
    self.move_vertical(GameConstants.BASE_JUMP_FORCE,GameConstants.ZERO_FORCE_MODIFIER)

    #animation
    self.update_sprite_animation(self.state_machine.character.death_spritesheet[0],self.state_machine.character.death_spritesheet[2],False)

  #check state


  #animation
  def draw(self, surface):
    super().draw(surface)
    if self.current_sprite_index == len(self.state_machine.character.death_spritesheet[0])-1:
      if self.is_show_last_frame and self.is_last_frame_animation_cooldown_finished:
        self.state_machine.character.is_running_death_animation = False
        self.is_show_last_frame = False
      else:
        self.is_show_last_frame = True
    

    offsetx = self.state_machine.character.death_spritesheet[3] * self.state_machine.character.death_spritesheet[1] 
    if self.state_machine.character.flip:
      offsetx = self.state_machine.character.death_spritesheet[4] * self.state_machine.character.death_spritesheet[1]
    offsety = self.state_machine.character.death_spritesheet[5] * self.state_machine.character.death_spritesheet[1]

    img = pygame.transform.flip(self.state_machine.character.death_spritesheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))




    
 