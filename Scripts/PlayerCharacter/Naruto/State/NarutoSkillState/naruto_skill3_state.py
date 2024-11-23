from Scripts.PlayerCharacter.Base.State.SkillState.skill_state import SkillState
from Scripts.game_constants import GameConstants
import pygame
from Scripts.FlyObject.energy_ball import EnergyBall
from Scripts.Audio.audio_manager import AudioManager
class NarutoSkill3State(SkillState):
  def enter(self):
    super().enter()
    AudioManager.get_instance().play_sfx(self.state_machine.character.skill_3_sfx_name)
    self.skill_collider_animations = GameConstants.NARUTO_SKILL3_COLLIDER_ANIMATIONS
    self.update_knock_back_force_target([5,20],150)
    self.is_fire_energy_ball = False
  def exit(self):
    AudioManager.get_instance().stop_sfx(self.state_machine.character.skill_3_sfx_name)
    super().exit()

  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.skill3_spritesheet[0],self.state_machine.character.skill3_spritesheet[2],False)


  def skill_attack(self):
    super().skill_attack()
    if not self.state_machine.character.is_using_skill:
      #execute attack
      self.state_machine.character.is_using_skill = True

  # animation
  def draw(self, surface):
    super().draw(surface)
    self.draw_skill_animation(surface,self.state_machine.character.skill3_spritesheet,GameConstants.NARUTO_SKILL3_COLLIDER_DICTIONARY)

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

    # tạo 1 energy ball add vào pool rồi pool sẽ tự động update trạng thái của energy ball
    if self.current_sprite_index == len(skill_sprite_sheet[0])-1 and not self.is_fire_energy_ball:
      #xét vị trí cầu dựa trên điêm trung tâm player
      posX = (self.state_machine.character.rect.centerx + 70) if not self.state_machine.character.flip else (self.state_machine.character.rect.centerx - 70 - GameConstants.NARUTO_ENERGY_BALL_SIZE[0])
      
      energyball = EnergyBall([posX,self.state_machine.character.rect.centery-42,GameConstants.NARUTO_ENERGY_BALL_SIZE[0],GameConstants.NARUTO_ENERGY_BALL_SIZE[1]],[-GameConstants.NARUTO_ENERGY_BALL_SPEED if self.state_machine.character.flip else GameConstants.NARUTO_ENERGY_BALL_SPEED,0],self.state_machine.character,self.state_machine.character.target,self.state_machine.screen_surface,self.state_machine.character.energy_ball_sprite_sheet)
      self.state_machine.character.energy_ball_pool.append(energyball)
      self.is_fire_energy_ball = True