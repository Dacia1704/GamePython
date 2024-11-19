from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
class HitState(CharacterState):
  def __init__(self, state_machine):
    super().__init__(state_machine)

  def enter(self):
    super().enter()
    #print("Enter hit")
    self.state_machine.character.health -= self.state_machine.character.dam_take
    self.start_knockback()




  def exit(self):
    super().exit()
    self.state_machine.character.reset_damable()

  def update(self):
    super().update()
    #check state
    # print(self.state_machine.character.is_hitting, self.state_machine.character.is_knockbacking)
    if not self.state_machine.character.is_hitting and not self.state_machine.character.is_knockbacking:
      self.on_nomal_attack()
      self.on_fall()
      self.on_jump()
      self.on_move()
      self.on_idle()

    #logic
    self.knockback()

    #animation
    self.update_sprite_animation(self.state_machine.character.hit_spritesheet[0],self.state_machine.character.hit_spritesheet[2],False)

  #check state


  #animation
  def draw(self, surface):
    super().draw(surface)
    if self.current_sprite_index == len(self.state_machine.character.hit_spritesheet[0])-1:
      if self.is_show_last_frame and self.is_last_frame_animation_cooldown_finished:
        self.state_machine.character.is_hitting = False
        self.is_show_last_frame = False
      else:
        self.is_show_last_frame = True
    

    offsetx = self.state_machine.character.hit_spritesheet[3] * self.state_machine.character.hit_spritesheet[1] 
    if self.state_machine.character.flip:
      offsetx = self.state_machine.character.hit_spritesheet[4] * self.state_machine.character.hit_spritesheet[1]
    offsety = self.state_machine.character.hit_spritesheet[5] * self.state_machine.character.hit_spritesheet[1]

    img = pygame.transform.flip(self.state_machine.character.hit_spritesheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))





    
 