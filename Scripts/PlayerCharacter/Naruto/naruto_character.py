from Scripts.PlayerCharacter.Base.character_base import Character
import pygame
from Scripts.game_constants import GameConstants
from Scripts.PlayerCharacter.Naruto.State.naruto_state_machine import NarutoStateMachine
class NarutoCharacter(Character):
  def __init__(self,player_id,x,y,screen_surface,target):
    super().__init__(player_id,x,y,screen_surface,target)
    self.rect = pygame.Rect((x,y,GameConstants.NARUTO_WIDTH_RECT,GameConstants.NARUTO_HEIGHT_RECT))
    self.state_machine = NarutoStateMachine(self,screen_surface)

    self.energy_ball_pool = []
    self.energy_ball_sprite_sheet = None

  def start(self):
    self.idle_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),34,50,6,GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[5]]
    self.move_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,6,GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[5]]
    self.jump_spritesheet= [self.handle_image(pygame.image.load(GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[0]).convert_alpha(),33,53,2,GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[5]]
    self.fall_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[0]).convert_alpha(),39,55,2,GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[5]]
    self.nomal_attack1_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[0]).convert_alpha(),56,48,4,GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[5]]
    self.nomal_attack2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,4,GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[5]]
    self.nomal_attack3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[0]).convert_alpha(),48,54,4,GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[5]]
    self.hit_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_HIT_SPRITESHEET_SOURCE[0]).convert_alpha(),48,47,2,GameConstants.NARUTO_HIT_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_HIT_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_HIT_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_HIT_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_HIT_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_HIT_SPRITESHEET_SOURCE[5]]
    self.dash_spritesheet = []
    self.skill1_spritesheet =[self.handle_image(pygame.image.load(GameConstants.NARUTO_SKILL1_SPRITESHEET_SOURCE[0]).convert_alpha(),48,64,8,GameConstants.NARUTO_SKILL1_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_SKILL1_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_SKILL1_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_SKILL1_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_SKILL1_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_SKILL1_SPRITESHEET_SOURCE[5]]
    self.skill2_spritesheet =[self.handle_image(pygame.image.load(GameConstants.NARUTO_SKILL2_SPRITESHEET_SOURCE[0]).convert_alpha(),64,80,12,GameConstants.NARUTO_SKILL2_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_SKILL2_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_SKILL2_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_SKILL2_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_SKILL2_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_SKILL2_SPRITESHEET_SOURCE[5]]
    self.skill3_spritesheet =[self.handle_image(pygame.image.load(GameConstants.NARUTO_SKILL3_SPRITESHEET_SOURCE[0]).convert_alpha(),80,48,14,GameConstants.NARUTO_SKILL3_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_SKILL3_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_SKILL3_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_SKILL3_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_SKILL3_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_SKILL3_SPRITESHEET_SOURCE[5]]
    self.energy_ball_sprite_sheet =[self.handle_image(pygame.image.load(GameConstants.NARUTO_ENERGY_BALL_SPRITESHEET_SOURCE[0]).convert_alpha(),55,55,4,GameConstants.NARUTO_ENERGY_BALL_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_ENERGY_BALL_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_ENERGY_BALL_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_ENERGY_BALL_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_ENERGY_BALL_SPRITESHEET_SOURCE[4],GameConstants.NARUTO_ENERGY_BALL_SPRITESHEET_SOURCE[5]]
    
    self.move_sfx_name = self.setup_sfx("move",GameConstants.NARUTO_MOVE_SFX[0])
    self.jump_sfx_name = self.setup_sfx("jump",GameConstants.NARUTO_JUMP_SFX[0])
    self.hit_sfx_name = self.setup_sfx("hit",GameConstants.NARUTO_HIT_SFX[0])
    self.death_sfx_name = self.setup_sfx("death",GameConstants.NARUTO_DEATH_SFX[0])
    self.nomal_attack_1_sfx_name = self.setup_sfx("nomal_attack_1",GameConstants.NARUTO_ATTACK1_SFX[0])
    self.nomal_attack_2_sfx_name = self.setup_sfx("nomal_attack_2",GameConstants.NARUTO_ATTACK2_SFX[0])
    self.nomal_attack_3_sfx_name = self.setup_sfx("nomal_attack_3",GameConstants.NARUTO_ATTACK3_SFX[0])
    self.skill_1_sfx_name = self.setup_sfx("skill_1",GameConstants.NARUTO_SKILL1_SFX[0])
    self.skill_2_sfx_name = self.setup_sfx("skill_2",GameConstants.NARUTO_SKILL2_SFX[0])
    self.skill_3_sfx_name = self.setup_sfx("skill_3",GameConstants.NARUTO_SKILL3_SFX[0])
    
    
    
    
    super().start()



  def update(self):
    super().update()
    
    #update trạng thái từng ball
    for energy_ball in self.energy_ball_pool:
      if energy_ball.is_hitting or energy_ball.is_out_screen:
        self.energy_ball_pool.remove(energy_ball)
      else: 
        energy_ball.update()
        