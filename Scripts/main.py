import pygame
from Scripts.game_constants import GameConstants
from Scripts.Input.game_input import GameInput
from Scripts.PlayerCharacter.Naruto.naruto_character import NarutoCharacter
from Scripts.PlayerCharacter.Sasuke.sasuke_character import SasukeCharacter
from Scripts.FlyObject.energy_ball import EnergyBall
from Scripts.PlayerCharacter.RockLee.rocklee_character import RockLeeCharacter
from Scripts.PlayerCharacter.Sakura.sakura_character import SakuraCharacter
from Scripts.Scene.scene_manager import SceneManager


pygame.init()
screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
pygame.display.set_caption("Infinity Fighter")
#clock
clock = pygame.time.Clock()
manager = SceneManager(screen)

running = True
while running:
  clock.tick(GameConstants.FPS)

  events = pygame.event.get()
  running = manager.handle_events(events)
  manager.update()
  pygame.display.flip()


#exit pygame
pygame.quit()
