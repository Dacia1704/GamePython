import pygame
from Scripts.game_constants import GameConstants
from Scripts.Input.game_input import GameInput
from Scripts.PlayerCharacter.Naruto.naruto_character import NarutoCharacter
from Scripts.PlayerCharacter.Sasuke.sasuke_character import SasukeCharacter
from Scripts.FlyObject.energy_ball import EnergyBall
from Scripts.PlayerCharacter.RockLee.rocklee_character import RockLeeCharacter
pygame.init()
screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
pygame.display.set_caption("Infinity Fighter")

#load bg images
HOKAGE_STATE_BG_IMAGE = pygame.image.load(GameConstants.HOKAGE_STATE_BG_IMAGE_SOURCE).convert_alpha()
RIVER_BG_IMAGE = pygame.image.load(GameConstants.RIVER_BG_IMAGE_SOURCE).convert_alpha()
SUMMER_VILLAGE_BG_IMAGE = pygame.image.load(GameConstants.SUMMER_VILLAGE_BG_IMAGE_SOURCE).convert_alpha()
WINTER_VILLAGE_BG_IMAGE = pygame.image.load(GameConstants.WINTER_VILLAGE_BG_IMAGE_SOURCE).convert_alpha()

#clock
clock = pygame.time.Clock()

#function for drawing background
def draw_bg():
  scaled_bg = pygame.transform.scale(SUMMER_VILLAGE_BG_IMAGE, (GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))

#player
player2 = NarutoCharacter(2,1000,GameConstants.SCREEN_HEIGHT-GameConstants.GROUND_Y,screen,None)
#player1 = NarutoCharacter(1,200,GameConstants.SCREEN_HEIGHT-GameConstants.GROUND_Y,screen,player2)
player1 = RockLeeCharacter(1,200,GameConstants.SCREEN_HEIGHT-GameConstants.GROUND_Y,screen,player2)

#update lại target
player2.target = player1


player1.start()
player2.start()


run = True
while run:

  clock.tick(GameConstants.FPS)

  #draw_bg
  draw_bg()

  #input update
  GameInput.get_instance().update()
  
  #player
  player1.update()
  player2.update()


  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


  #update display
  pygame.display.update()
#exit pygame
pygame.quit()
