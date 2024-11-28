from Scripts.PlayerCharacter.Base.character_base import Character
import pygame
from Scripts.game_constants import GameConstants
from Scripts.PlayerCharacter.Sasuke.State.sasuke_state_machine import SasukeStateMachine
class SasukeCharacter(Character):
  def __init__(self,game_scene,player_id,x,y,screen_surface,target):
    super().__init__(game_scene,player_id,x,y,screen_surface,target)
    self.rect = pygame.Rect((x,y,GameConstants.SASUKE_WIDTH_RECT,GameConstants.SASUKE_HEIGHT_RECT))
    self.state_machine = SasukeStateMachine(self,screen_surface)

    self.energy_ball_pool = []
    self.energy_ball_sprite_sheet = None
  
  def start(self):
    self.idle_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),34,50,6,GameConstants.SASUKE_IDLE_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_IDLE_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_IDLE_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_IDLE_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_IDLE_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_IDLE_SPRITESHEET_SOURCE[5]]
    self.move_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_MOVE_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,6,GameConstants.SASUKE_MOVE_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_MOVE_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_MOVE_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_MOVE_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_MOVE_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_MOVE_SPRITESHEET_SOURCE[5]]
    self.jump_spritesheet= [self.handle_image(pygame.image.load(GameConstants.SASUKE_JUMP_SPRITESHEET_SOURCE[0]).convert_alpha(),33,53,2,GameConstants.SASUKE_JUMP_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_JUMP_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_JUMP_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_JUMP_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_JUMP_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_JUMP_SPRITESHEET_SOURCE[5]]
    self.fall_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_FALL_SPRITESHEET_SOURCE[0]).convert_alpha(),35,55,2,GameConstants.SASUKE_FALL_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_FALL_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_FALL_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_FALL_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_FALL_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_FALL_SPRITESHEET_SOURCE[5]]
    self.nomal_attack1_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_ATTACK1_SPRITESHEET_SOURCE[0]).convert_alpha(),56,48,4,GameConstants.SASUKE_ATTACK1_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_ATTACK1_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_ATTACK1_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_ATTACK1_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_ATTACK1_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_ATTACK1_SPRITESHEET_SOURCE[5]]
    self.nomal_attack2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_ATTACK2_SPRITESHEET_SOURCE[0]).convert_alpha(),56,48,4,GameConstants.SASUKE_ATTACK2_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_ATTACK2_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_ATTACK2_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_ATTACK2_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_ATTACK2_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_ATTACK2_SPRITESHEET_SOURCE[5]]
    self.nomal_attack3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_ATTACK3_SPRITESHEET_SOURCE[0]).convert_alpha(),56,48,4,GameConstants.SASUKE_ATTACK3_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_ATTACK3_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_ATTACK3_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_ATTACK3_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_ATTACK3_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_ATTACK3_SPRITESHEET_SOURCE[5]]
    self.hit_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_HIT_SPRITESHEET_SOURCE[0]).convert_alpha(),48,47,2,GameConstants.SASUKE_HIT_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_HIT_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_HIT_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_HIT_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_HIT_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_HIT_SPRITESHEET_SOURCE[5]]
    self.dash_spritesheet=[self.handle_image(pygame.image.load(GameConstants.SASUKE_DASH_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,6,GameConstants.SASUKE_DASH_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_DASH_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_DASH_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_DASH_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_DASH_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_DASH_SPRITESHEET_SOURCE[5]]
    self.death_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_DEATH_SPRITESHEET_SOURCE[0]).convert_alpha(),60,38,3,GameConstants.SASUKE_DEATH_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_DEATH_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_DEATH_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_DEATH_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_DEATH_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_DEATH_SPRITESHEET_SOURCE[5]]
    self.skill1_spritesheet =[self.handle_image(pygame.image.load(GameConstants.SASUKE_SKILL1_SPRITESHEET_SOURCE[0]).convert_alpha(),80,48,14,GameConstants.SASUKE_SKILL1_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_SKILL1_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_SKILL1_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_SKILL1_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_SKILL1_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_SKILL1_SPRITESHEET_SOURCE[5]]
    self.energy_ball_sprite_sheet =[self.handle_image(pygame.image.load(GameConstants.SASUKE_ENERGY_BALL_SPRITESHEET_SOURCE[0]).convert_alpha(),55,55,4,GameConstants.SASUKE_ENERGY_BALL_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_ENERGY_BALL_SPRITESHEET_SOURCE[1],GameConstants.SASUKE_ENERGY_BALL_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_ENERGY_BALL_SPRITESHEET_SOURCE[3],GameConstants.SASUKE_ENERGY_BALL_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_ENERGY_BALL_SPRITESHEET_SOURCE[5]]
    print(self.energy_ball_sprite_sheet)
    self.skill2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_SKILL2_SPRITESHEET_SOURCE[0]).convert_alpha(), 74, 44, 15,GameConstants.SASUKE_SKILL2_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_SKILL2_SPRITESHEET_SOURCE[1], GameConstants.SASUKE_SKILL2_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_SKILL2_SPRITESHEET_SOURCE[3], GameConstants.SASUKE_SKILL2_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_SKILL2_SPRITESHEET_SOURCE[5]]
    self.skill3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SASUKE_SKILL3_SPRITESHEET_SOURCE[0]).convert_alpha(), 226, 64, 12, GameConstants.SASUKE_SKILL3_SPRITESHEET_SOURCE[1]),GameConstants.SASUKE_SKILL3_SPRITESHEET_SOURCE[1], GameConstants.SASUKE_SKILL3_SPRITESHEET_SOURCE[2],GameConstants.SASUKE_SKILL3_SPRITESHEET_SOURCE[3], GameConstants.SASUKE_SKILL3_SPRITESHEET_SOURCE[4],GameConstants.SASUKE_SKILL3_SPRITESHEET_SOURCE[5]]
    
    self.mana_consume_skill_1 = GameConstants.SASUKE_SKILL_1_PROPS[1]
    self.mana_consume_skill_2 = GameConstants.SASUKE_SKILL_2_PROPS[1]
    self.mana_consume_skill_3 = GameConstants.SASUKE_SKILL_3_PROPS[1]

    self.move_sfx_name = self.setup_sfx("sasuke_move",GameConstants.SASUKE_MOVE_SFX[0])
    self.jump_sfx_name = self.setup_sfx("sasuke_jump",GameConstants.SASUKE_JUMP_SFX[0])
    self.hit_sfx_name = self.setup_sfx("sasuke_hit",GameConstants.SASUKE_HIT_SFX[0])
    self.death_sfx_name = self.setup_sfx("sasuke_death",GameConstants.SASUKE_DEATH_SFX[0])
    self.dash_sfx_name = self.setup_sfx("sasuke_dash",GameConstants.SASUKE_DASH_SFX[0])
    self.nomal_attack_1_sfx_name = self.setup_sfx("sasuke_nomal_attack_1",GameConstants.SASUKE_ATTACK1_SFX[0])
    self.nomal_attack_2_sfx_name = self.setup_sfx("sasuke_nomal_attack_2",GameConstants.SASUKE_ATTACK2_SFX[0])
    self.nomal_attack_3_sfx_name = self.setup_sfx("sasuke_nomal_attack_3",GameConstants.SASUKE_ATTACK3_SFX[0])
    self.skill_1_sfx_name = self.setup_sfx("sasuke_skill_1",GameConstants.SASUKE_SKILL1_SFX[0])
    self.skill_2_sfx_name = self.setup_sfx("sasuke_skill_2",GameConstants.SASUKE_SKILL2_SFX[0])
    self.skill_3_sfx_name = self.setup_sfx("sasuke_skill_3",GameConstants.SASUKE_SKILL3_SFX[0])
    
    super().start()
  def update(self):
    super().update()
  
    #update trạng thái từng ball
    for energy_ball in self.energy_ball_pool:
      if energy_ball.is_hitting or energy_ball.is_out_screen:
        self.energy_ball_pool.remove(energy_ball)
      else: 
        energy_ball.update()

  
    