from Scripts.PlayerCharacter.Base.character_base import Character
import pygame
from Scripts.game_constants import GameConstants
from Scripts.PlayerCharacter.RockLee.State.rocklee_state_machine import RockLeeStateMachine
class RockLeeCharacter(Character):
  def __init__(self,x,y,screen_surface):
    super().__init__(x,y,screen_surface)
    self.rect = pygame.Rect((x,y,GameConstants.ROCKLEE_WIDTH_RECT,GameConstants.ROCKLEE_HEIGHT_RECT))
    self.state_machine = RockLeeStateMachine(self,screen_surface)

  def start(self):
    self.idle_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),34,50,6,GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_IDLE_SPRITESHEET_SOURCE[4]]
    self.move_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,6,GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_MOVE_SPRITESHEET_SOURCE[4]]
    self.jump_spritesheet= [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[0]).convert_alpha(),33,53,2,GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_JUMP_SPRITESHEET_SOURCE[4]]
    self.fall_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[0]).convert_alpha(),39,55,2,GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_FALL_SPRITESHEET_SOURCE[4]]
    self.nomal_attack1_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[0]).convert_alpha(),56,48,4,GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_ATTACK1_SPRITESHEET_SOURCE[5]]
    self.nomal_attack2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,4,GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_ATTACK2_SPRITESHEET_SOURCE[5]]
    self.nomal_attack3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[0]).convert_alpha(),48,54,4,GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[1]),GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[1],GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[2],GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[3],GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[4],GameConstants.ROCKLEE_ATTACK3_SPRITESHEET_SOURCE[5]]

    super().start()