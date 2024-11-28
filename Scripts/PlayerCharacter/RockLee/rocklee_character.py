from Scripts.PlayerCharacter.Base.character_base import Character
import pygame
from Scripts.game_constants import GameConstants
from Scripts.PlayerCharacter.RockLee.State.rocklee_state_machine import RockLeeStateMachine
class RockLeeCharacter(Character):
  def __init__(self,game_scene,player_id,x,y,screen_surface,target):
    super().__init__(game_scene,player_id,x,y,screen_surface,target)
    self.rect = pygame.Rect((x,y,GameConstants.ROCKLEE_WIDTH_RECT,GameConstants.ROCKLEE_HEIGHT_RECT))
    self.state_machine = RockLeeStateMachine(self,screen_surface)

  def start(self):
    self.idle_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),33,48,4,GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[5]]
    self.move_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[0]).convert_alpha(),41,40,6,GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[5]]
    self.jump_spritesheet= [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[0]).convert_alpha(),25,48,2,GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[5]]
    self.fall_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[0]).convert_alpha(),33,40,2,GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[5]]
    self.nomal_attack1_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[0]).convert_alpha(),51,48,4,GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[5]]
    self.nomal_attack2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[0]).convert_alpha(),60,48,4,GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[5]]
    self.nomal_attack3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[0]).convert_alpha(),57,48,4,GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[5]]
    self.hit_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_HIT_SPRITESHEET_SOURCE[0]).convert_alpha(),41,40,2,GameConstants.ROCKLEE_HIT_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_HIT_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_HIT_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_HIT_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_HIT_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_HIT_SPRITESHEET_SOURCE[5]]
    self.dash_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_DASH_SPRITESHEET_SOURCE[0]).convert_alpha(),33,48,4,GameConstants.ROCKLEE_DASH_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_DASH_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_DASH_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_DASH_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_DASH_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_DASH_SPRITESHEET_SOURCE[5]]
    
    self.skill1_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_SKILL1_SPRITESHEET_SOURCE[0]).convert_alpha(),73,65,7,GameConstants.ROCKLEE_SKILL1_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_SKILL1_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_SKILL1_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_SKILL1_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_SKILL1_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_SKILL1_SPRITESHEET_SOURCE[5]]
    self.skill2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_SKILL2_SPRITESHEET_SOURCE[0]).convert_alpha(),96,65,8,GameConstants.ROCKLEE_SKILL2_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_SKILL2_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_SKILL2_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_SKILL2_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_SKILL2_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_SKILL2_SPRITESHEET_SOURCE[5]]
    self.skill3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_SKILL3_SPRITESHEET_SOURCE[0]).convert_alpha(),96,65,5,GameConstants.ROCKLEE_SKILL3_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_SKILL3_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_SKILL3_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_SKILL3_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_SKILL3_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_SKILL3_SPRITESHEET_SOURCE[5]]
    
    self.move_sfx_name = self.setup_sfx("move",GameConstants.ROCKLEE_MOVE_SFX[0])
    self.jump_sfx_name = self.setup_sfx("jump",GameConstants.ROCKLEE_JUMP_SFX[0])
    self.hit_sfx_name = self.setup_sfx("hit",GameConstants.ROCKLEE_HIT_SFX[0])
    self.death_sfx_name = self.setup_sfx("death",GameConstants.ROCKLEE_DEATH_SFX[0])
    self.nomal_attack_1_sfx_name = self.setup_sfx("attack1",GameConstants.ROCKLEE_ATTACK1_SFX[0])
    self.nomal_attack_2_sfx_name = self.setup_sfx("attack2",GameConstants.ROCKLEE_ATTACK2_SFX[0])
    self.nomal_attack_3_sfx_name = self.setup_sfx("attack3",GameConstants.ROCKLEE_ATTACK3_SFX[0])
    self.skill_1_sfx_name = self.setup_sfx("skill1",GameConstants.ROCKLEE_SKILL1_SFX[0])
    self.skill_2_sfx_name = self.setup_sfx("skill2",GameConstants.ROCKLEE_SKILL2_SFX[0])
    self.skill_3_sfx_name = self.setup_sfx("skill3",GameConstants.ROCKLEE_SKILL3_SFX[0])
    self.dash_sfx_name = self.setup_sfx("rocklee_dash",GameConstants.ROCKLEE_DASH_SFX[0])
    
    self.death_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_DEATH_SPRITESHEET_SOURCE[0]).convert_alpha(),51,35,3,GameConstants.ROCKLEE_DEATH_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_DEATH_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_DEATH_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_DEATH_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_DEATH_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_DEATH_SPRITESHEET_SOURCE[5]]
    super().start()