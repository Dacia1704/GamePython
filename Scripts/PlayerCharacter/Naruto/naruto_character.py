from Scripts.PlayerCharacter.Base.character_base import Character
import pygame
from Scripts.game_constants import GameConstants
from Scripts.PlayerCharacter.Naruto.State.naruto_state_machine import NarutoStateMachine
class NarutoCharacter(Character):
  def __init__(self,x,y,screen_surface):
    super().__init__(x,y,screen_surface)
    self.rect = pygame.Rect((x,y,GameConstants.NARUTO_WIDTH_RECT,GameConstants.NARUTO_HEIGHT_RECT))
    self.state_machine = NarutoStateMachine(self,screen_surface)

  def start(self):
    self.idle_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),34,50,6,GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[4]]
    self.move_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,6,GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[4]]
    self.jump_spritesheet= [self.handle_image(pygame.image.load(GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[0]).convert_alpha(),33,53,2,GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[4]]
    self.fall_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[0]).convert_alpha(),39,55,2,GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[4]]
    self.nomal_attack1_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[0]).convert_alpha(),56,48,4,GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_ATTACK1_SPRITESHEET_SOURCE[4]]
    self.nomal_attack2_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,4,GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_ATTACK2_SPRITESHEET_SOURCE[4]]
    self.nomal_attack3_spritesheet = [self.handle_image(pygame.image.load(GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[0]).convert_alpha(),48,54,4,GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[1]),GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[1],GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[2],GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[3],GameConstants.NARUTO_ATTACK3_SPRITESHEET_SOURCE[4]]

    super().start()