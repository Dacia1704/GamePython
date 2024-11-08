from Scripts.PlayerCharacter.Base.character_base import Character
import pygame
from Scripts.game_constants import GameConstants
class NarutoCharacter(Character):
  def start(self):
    super().start()
    self.idle_spritesheet = self.handle_image(pygame.image.load(GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[0]).convert_alpha(),34,50,6,GameConstants.NARUTO_IDLE_SPRITESHEET_SOURCE[1])
    self.move_spritesheet = self.handle_image(pygame.image.load(GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[0]).convert_alpha(),48,48,6,GameConstants.NARUTO_MOVE_SPRITESHEET_SOURCE[1])
    self.jump_spritesheet = self.handle_image(pygame.image.load(GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[0]).convert_alpha(),33,53,2,GameConstants.NARUTO_JUMP_SPRITESHEET_SOURCE[1])
    self.fall_spritesheet = self.handle_image(pygame.image.load(GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[0]).convert_alpha(),39,55,2,GameConstants.NARUTO_FALL_SPRITESHEET_SOURCE[1])