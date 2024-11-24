from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants
import pygame
import random
class NomalAttackState(CharacterState):
  def __init__(self, state_machine):
    super().__init__(state_machine)

    self.attack_collider_animations = []

    self.is_add_mana = False


  #base function
  def enter(self):
    super().enter()
    #print("Enter Nomal Attack")
    self.update_knock_back_force_target([GameConstants.NOMAL_ATTACK_PROPS[2][0],GameConstants.NOMAL_ATTACK_PROPS[2][1]],GameConstants.NOMAL_ATTACK_PROPS[3])
    self.update_target_dam_take(GameConstants.NOMAL_ATTACK_PROPS[0])
    self.nomal_attack_enter()
    self.is_add_mana = False


  def exit(self):
    super().exit()
    #print("Exit Nomal Attack")

  def update(self):
    super().update()
    #check state
    if not self.state_machine.character.is_nomal_attacking:
      self.on_jump()
      self.on_move()
      self.on_idle() 
      self.on_skill1()
      self.on_skill2()
      self.on_skill3()

    #logic
    self.nomal_attack()

  def nomal_attack(self):
    if self.state_machine.character.is_hitting and not self.is_add_mana:
      self.state_machine.character.mana +=5
      self.is_add_mana = True
    pass

  def nomal_attack_enter(self):
    pass

  #draw
  def draw_attack_animation(self, surface,sprite_sheet_data,animation_collider_dictionary):
    nomal_attack_sprite_sheet = sprite_sheet_data
    
    #kiem tra va cai dat lai chi so khung hinh neu vuot qua list
    #if self.current_sprite_index >= len(nomal_attack_sprite_sheet[0]):
    #    self.current_sprite_index = 0
        
    if self.current_sprite_index == len(nomal_attack_sprite_sheet[0])-1:
      if self.is_show_last_frame and self.is_last_frame_animation_cooldown_finished:
        self.state_machine.character.is_nomal_attacking = False
        self.is_show_last_frame = False
      else:
        self.is_show_last_frame = True
    
    offsetx = nomal_attack_sprite_sheet[3] * nomal_attack_sprite_sheet[1] 
    if self.state_machine.character.flip:
      offsetx = nomal_attack_sprite_sheet[4] * nomal_attack_sprite_sheet[1]
    offsety = nomal_attack_sprite_sheet[5] * nomal_attack_sprite_sheet[1]

    img = pygame.transform.flip(nomal_attack_sprite_sheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))

    if self.current_sprite_index in self.attack_collider_animations:
      collider_rect_props = animation_collider_dictionary.get(self.current_sprite_index)
      self.state_machine.character.draw_attack_area_collider(collider_rect_props[0], collider_rect_props[1],self.state_machine.character.target)



    


