from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
import random
class SkillState(CharacterState):
  def __init__(self, state_machine):
    super().__init__(state_machine)

    self.skill_collider_animations = []


  #base function
  def enter(self):
    super().enter()
    print("SKillAttack")

  def exit(self):
    super().exit()
    print("Exit skill Attack")

  def update(self):
    super().update()
    #check state
    if not self.state_machine.character.is_using_skill:
      self.on_jump()
      self.on_move()
      self.on_idle()

    #logic
    self.skill_attack()

  def skill_attack(self):
    pass

  #draw
  def draw_skill_animation(self, surface,sprite_sheet_data,animation_collider_dictionary):
    skill_sprite_sheet = sprite_sheet_data

    if self.current_sprite_index == len(skill_sprite_sheet[0])-1:
      if self.is_show_last_frame and self.is_last_frame_animation_cooldown_finished:
        self.state_machine.character.is_using_skill = False
        self.is_show_last_frame = False
      else:
        self.is_show_last_frame = True
    
    offsetx = skill_sprite_sheet[3] * skill_sprite_sheet[1] 
    if self.state_machine.character.flip:
      offsetx = skill_sprite_sheet[4] * skill_sprite_sheet[1]
    offsety = skill_sprite_sheet[5] * skill_sprite_sheet[1]

    img = pygame.transform.flip(skill_sprite_sheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))

    if self.current_sprite_index in self.skill_collider_animations:
      collider_rect_props = animation_collider_dictionary.get(self.current_sprite_index)
      self.state_machine.character.draw_attack_area_collider(collider_rect_props[0], collider_rect_props[1],self.state_machine.character.target)

    

    


