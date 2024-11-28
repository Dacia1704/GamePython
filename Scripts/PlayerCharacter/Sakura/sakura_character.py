from Scripts.PlayerCharacter.Base.character_base import Character
import pygame
from Scripts.game_constants import GameConstants
from Scripts.PlayerCharacter.Sakura.State.sakura_state_machine import SakuraStateMachine
class SakuraCharacter(Character):
  def __init__(self,player_id,x,y,screen_surface,target):
    super().__init__(player_id,x,y,screen_surface,target)
    self.rect = pygame.Rect((x,y,GameConstants.SAKURA_WIDTH_RECT,GameConstants.SAKURA_HEIGHT_RECT))
    self.state_machine = SakuraStateMachine(self,screen_surface)

  def start(self):
    self.idle_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),34,49,6,GameConstants.SAKURA_IDLE_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_IDLE_SPRITESHEET_SOURCE[1],GameConstants.SAKURA_IDLE_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_IDLE_SPRITESHEET_SOURCE[3],GameConstants.SAKURA_IDLE_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_IDLE_SPRITESHEET_SOURCE[5]]
    self.move_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_MOVE_SPRITESHEET_SOURCE[0]).convert_alpha(),50,48,6,GameConstants.SAKURA_MOVE_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_MOVE_SPRITESHEET_SOURCE[1],GameConstants.SAKURA_MOVE_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_MOVE_SPRITESHEET_SOURCE[3],GameConstants.SAKURA_MOVE_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_MOVE_SPRITESHEET_SOURCE[5]]
    self.jump_spritesheet= [self.handle_image(pygame.image.load(GameConstants.SAKURA_JUMP_SPRITESHEET_SOURCE[0]).convert_alpha(),34,48,2,GameConstants.SAKURA_JUMP_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_JUMP_SPRITESHEET_SOURCE[1],GameConstants.SAKURA_JUMP_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_JUMP_SPRITESHEET_SOURCE[3],GameConstants.SAKURA_JUMP_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_JUMP_SPRITESHEET_SOURCE[5]]
    self.fall_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_FALL_SPRITESHEET_SOURCE[0]).convert_alpha(),40,48,2,GameConstants.SAKURA_FALL_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_FALL_SPRITESHEET_SOURCE[1],GameConstants.SAKURA_FALL_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_FALL_SPRITESHEET_SOURCE[3],GameConstants.SAKURA_FALL_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_FALL_SPRITESHEET_SOURCE[5]]
    self.nomal_attack1_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_ATTACK1_SPRITESHEET_SOURCE[0]).convert_alpha(),62,48,4,GameConstants.SAKURA_ATTACK1_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_ATTACK1_SPRITESHEET_SOURCE[1],GameConstants.SAKURA_ATTACK1_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_ATTACK1_SPRITESHEET_SOURCE[3],GameConstants.SAKURA_ATTACK1_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_ATTACK1_SPRITESHEET_SOURCE[5]]
    self.nomal_attack2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_ATTACK2_SPRITESHEET_SOURCE[0]).convert_alpha(),53,49,4,GameConstants.SAKURA_ATTACK2_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_ATTACK2_SPRITESHEET_SOURCE[1],GameConstants.SAKURA_ATTACK2_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_ATTACK2_SPRITESHEET_SOURCE[3],GameConstants.SAKURA_ATTACK2_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_ATTACK2_SPRITESHEET_SOURCE[5]]
    self.nomal_attack3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_ATTACK3_SPRITESHEET_SOURCE[0]).convert_alpha(),58,50,5,GameConstants.SAKURA_ATTACK3_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_ATTACK3_SPRITESHEET_SOURCE[1],GameConstants.SAKURA_ATTACK3_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_ATTACK3_SPRITESHEET_SOURCE[3],GameConstants.SAKURA_ATTACK3_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_ATTACK3_SPRITESHEET_SOURCE[5]]
    self.hit_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_HIT_SPRITESHEET_SOURCE[0]).convert_alpha(),39,40,2,GameConstants.SAKURA_HIT_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_HIT_SPRITESHEET_SOURCE[1],GameConstants.SAKURA_HIT_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_HIT_SPRITESHEET_SOURCE[3],GameConstants.SAKURA_HIT_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_HIT_SPRITESHEET_SOURCE[5]]
    self.skill1_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_SKILL1_SPRITESHEET_SOURCE[0]).convert_alpha(), 226, 64, 8,GameConstants.SAKURA_SKILL1_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_SKILL1_SPRITESHEET_SOURCE[1], GameConstants.SAKURA_SKILL1_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_SKILL1_SPRITESHEET_SOURCE[3], GameConstants.SAKURA_SKILL1_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_SKILL1_SPRITESHEET_SOURCE[5]]
    self.skill2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_SKILL2_SPRITESHEET_SOURCE[0]).convert_alpha(), 74, 44, 15,GameConstants.SAKURA_SKILL2_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_SKILL2_SPRITESHEET_SOURCE[1], GameConstants.SAKURA_SKILL2_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_SKILL2_SPRITESHEET_SOURCE[3], GameConstants.SAKURA_SKILL2_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_SKILL2_SPRITESHEET_SOURCE[5]]
    self.skill3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_SKILL3_SPRITESHEET_SOURCE[0]).convert_alpha(), 226, 64, 12, GameConstants.SAKURA_SKILL3_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_SKILL3_SPRITESHEET_SOURCE[1], GameConstants.SAKURA_SKILL3_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_SKILL3_SPRITESHEET_SOURCE[3], GameConstants.SAKURA_SKILL3_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_SKILL3_SPRITESHEET_SOURCE[5]]
    self.dash_spritesheet = [self.handle_image(pygame.image.load(GameConstants.SAKURA_DASH_SPRITESHEET_SOURCE[0]).convert_alpha(), 34, 49, 4,GameConstants.SAKURA_DASH_SPRITESHEET_SOURCE[1]),GameConstants.SAKURA_DASH_SPRITESHEET_SOURCE[1], GameConstants.SAKURA_DASH_SPRITESHEET_SOURCE[2],GameConstants.SAKURA_DASH_SPRITESHEET_SOURCE[3], GameConstants.SAKURA_DASH_SPRITESHEET_SOURCE[4],GameConstants.SAKURA_DASH_SPRITESHEET_SOURCE[5]]

    self.move_sfx_name = self.setup_sfx("move", GameConstants.SAKURA_MOVE_SFX[0])
    self.jump_sfx_name = self.setup_sfx("jump", GameConstants.SAKURA_JUMP_SFX[0])
    self.hit_sfx_name = self.setup_sfx("C2", GameConstants.SAKURA_HIT_SFX[0])
    self.death_sfx_name = self.setup_sfx("C2", GameConstants.SAKURA_DEATH_SFX[0])
    self.nomal_attack_1_sfx_name = self.setup_sfx("C1", GameConstants.SAKURA_ATTACK1_SFX[0])
    self.nomal_attack_2_sfx_name = self.setup_sfx("C4", GameConstants.SAKURA_ATTACK2_SFX[0])
    self.nomal_attack_3_sfx_name = self.setup_sfx("C3", GameConstants.SAKURA_ATTACK3_SFX[0])
    self.skill_1_sfx_name = self.setup_sfx("C2", GameConstants.SAKURA_SKILL1_SFX[0])
    self.skill_2_sfx_name = self.setup_sfx("R3", GameConstants.SAKURA_SKILL2_SFX[0])
    self.skill_3_sfx_name = self.setup_sfx("S1", GameConstants.SAKURA_SKILL3_SFX[0])

    self.mana_consume_skill_1 = GameConstants.SAKURA_SKILL_1_PROPS[1]
    self.mana_consume_skill_2 = GameConstants.SAKURA_SKILL_2_PROPS[1]
    self.mana_consume_skill_3 = GameConstants.SAKURA_SKILL_3_PROPS[1]

    super().start()