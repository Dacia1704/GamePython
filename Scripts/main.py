import pygame
from Scripts.game_constants import GameConstants
from Scripts.PlayerCharacter.character import Character
from Scripts.Input.game_input import GameInput

pygame.init()

screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
pygame.display.set_caption("Infinity Fighter")

#load bg images
HOKAGE_STATE_BG_IMAGE = pygame.image.load(GameConstants.hokage_state_bg_image_source).convert_alpha()
RIVER_BG_IMAGE = pygame.image.load(GameConstants.river_bg_image_source).convert_alpha()
SUMMER_VILLAGE_BG_IMAGE = pygame.image.load(GameConstants.summer_village_bg_image_source).convert_alpha()
WINTER_VILLAGE_BG_IMAGE = pygame.image.load(GameConstants.winter_village_bg_image_source).convert_alpha()

#clock
clock = pygame.time.Clock()

#function for drawing background
def draw_bg():
  scaled_bg = pygame.transform.scale(SUMMER_VILLAGE_BG_IMAGE, (GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))

#player
player1 = Character(200,310,screen)
player2 = Character(1000,310,screen)
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