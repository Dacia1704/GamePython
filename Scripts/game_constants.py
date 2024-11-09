import pygame
class GameConstants:
  #create game window
  SCREEN_WIDTH = 1280
  SCREEN_HEIGHT = 720

  #FPS default
  FPS = 60

  #Ground
  GROUND_Y = 250

  #define colours
  RED = (255, 0, 0)
  YELLOW = (255, 255, 0)
  WHITE = (255, 255, 255)

  # background image source
  HOKAGE_STATE_BG_IMAGE_SOURCE = "Assets/Background/hokage_state.jpg"
  RIVER_BG_IMAGE_SOURCE = "Assets/Background/river.jpg"
  SUMMER_VILLAGE_BG_IMAGE_SOURCE = "Assets/Background/summer_village.jpg"
  WINTER_VILLAGE_BG_IMAGE_SOURCE = "Assets/Background/winter_village.jpg"

  # naruto character image source
  NARUTO_WIDTH_RECT = 60
  NARUTO_HEIGHT_RECT = 110
  NARUTO_IDLE_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/idle_w34_h50.png",3,50,7,5]# 0:source, 1:scale, 2:animation cooldown,3:offsetx, 4:offsety
  NARUTO_MOVE_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/move_w48_h48.png",3,50,15,5]
  NARUTO_JUMP_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/jump_w33_h53.png",3,50,5,5]
  NARUTO_FALL_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/fall_w39_h55.png",3,50,5,5]
  NARUTO_ATTACK1_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/attack1_w56_h48.png",3,70,5,5]  
  NARUTO_ATTACK2_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/attack2_w48_h48.png",3,100,5,5]  
  NARUTO_ATTACK3_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/attack3_w48_h54.png",3,100,5,20]  


  # keyboard player1
  LEFT1 = pygame.K_a
  RIGHT1 = pygame.K_d
  UP1 = pygame.K_w
  DOWN1 = pygame.K_s
  NOMALATTACK1 = pygame.K_j
  SKILL1_1 = pygame.K_u
  SKILL2_1 = pygame.K_i
  SKILL3_1 = pygame.K_o

  # keyboad player2
  LEFT2 = pygame.K_LEFT
  RIGHT2 = pygame.K_RIGHT
  UP2 = pygame.K_UP
  DOWN2 = pygame.K_DOWN
  NOMALATTACK2 = pygame.K_KP0
  SKILL1_2 = pygame.K_KP1
  SKILL2_2 = pygame.K_KP2
  SKILL3_2 = pygame.K_KP3

  #base attribute
  GRAVITY = 2
  BASE_SPEED = 10
  BASE_JUMP_FORCE = 35
  IDLE_SPEED_MODIFIER = 0
  MOVE_SPEED_MODIFIER = 1
  JUMP_FORCE_MODIFIER = 1
  ZERO_FORCE_MODIFIER = 0
  BASE_HEALTH = 10
  TIME_RESET_ATTACK_COMBO = 2



  

