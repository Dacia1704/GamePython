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

  #UI
  RAW_BUTTON_IMAGE = ["Assets/UI/raw_button_w160_h85.png", 1]  #image, scale 

  #BGM
  MAIN_MENU_BGM = ["Assets/Music/main_menu_bgm.wav",True]
  BATTLE_1_BGM = ["Assets/Music/battle_1_bgm.mp3",True]
  BATTLE_2_BGM = ["Assets/Music/battle_2_bgm.mp3",True]
  BATTLE_3_BGM = ["Assets/Music/battle_3_bgm.mp3",True]

  #Font
  ROBOTO_BLACK_1 = ["Assets/Font/Roboto/Roboto-Black.ttf",30]
  ROBOTO_BLACK_2 = ["Assets/Font/Roboto/Roboto-Black.ttf",60]
  ROBOTO_BLACK_ITALIC_1 = ["Assets/Font/Roboto/Roboto-BlackItalic.ttf",30]
  ROBOTO_BOLD_1 = ["Assets/Font/Roboto/Roboto-Bold.ttf",30]
  ROBOTO_BOLD_ITALIC_1 = ["Assets/Font/Roboto/Roboto-BoldItalic.ttf",30]
  ROBOTO_ITALIC_1 = ["Assets/Font/Roboto/Roboto-Italic.ttf",30]
  ROBOTO_LIGHT_1 = ["Assets/Font/Roboto/Roboto-Light.ttf",30]
  ROBOTO_LIGHT_ITALIC_1 = ["Assets/Font/Roboto/Roboto-LightItalic.ttf",20]
  ROBOTO_MEDIUM_1 = ["Assets/Font/Roboto/Roboto-Medium.ttf",30]
  ROBOTO_MEDIUM_ITALIC_1 = ["Assets/Font/Roboto/Roboto-MediumItalic.ttf",30]
  ROBOTO_REGULAR_1 = ["Assets/Font/Roboto/Roboto-Regular.ttf",30]
  ROBOTO_THIN_1 = ["Assets/Font/Roboto/Roboto-Thin.ttf",30]
  ROBOTO_THIN_ITALIC_1 = ["Assets/Font/Roboto/Roboto-ThinItalic.ttf",30]

  PROTESTREVOLUTION_REGULAR_1 = ["Assets/Font/Protest_Revolution/ProtestRevolution-Regular.ttf",100]

  # naruto character image source and props
  NARUTO_WIDTH_RECT = 60
  NARUTO_HEIGHT_RECT = 110
  NARUTO_IDLE_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/idle_w34_h50.png",3,50,7,7,5]# 0:source, 1:scale, 2:animation cooldown,3:offsetx,4: offsetx flip, 5:offsety
  NARUTO_MOVE_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/move_w48_h48.png",3,50,15,15,5]
  NARUTO_JUMP_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/jump_w33_h53.png",3,50,5,5,5]
  NARUTO_FALL_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/fall_w39_h55.png",3,50,5,5,5]
  NARUTO_ATTACK1_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/attack1_w56_h48.png",3,100,10,25,2]  
  NARUTO_ATTACK1_COLLIDER_ANIMATIONS = [3]
  NARUTO_ATTACK1_COLLIDER_DICTIONARY = {
    3:[[NARUTO_WIDTH_RECT/2,-NARUTO_HEIGHT_RECT/2 + 20],[60,35]]
  }
  NARUTO_ATTACK2_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/attack2_w48_h48.png",3,100,5,23,5]  
  NARUTO_ATTACK2_COLLIDER_ANIMATIONS = [3]
  NARUTO_ATTACK2_COLLIDER_DICTIONARY = {
    3:[[NARUTO_WIDTH_RECT/2,-NARUTO_HEIGHT_RECT/2 + 20],[62,35]]   # animation_index: [[pos relate character center x, pos relate character center y],[width,height]]
  }
  NARUTO_ATTACK3_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/attack3_w48_h54.png",3,100,5,20,30]  
  NARUTO_ATTACK3_COLLIDER_ANIMATIONS = [2]
  NARUTO_ATTACK3_COLLIDER_DICTIONARY = {
    2:[[NARUTO_WIDTH_RECT/2,-NARUTO_HEIGHT_RECT/2- 5],[60,35]]
  }

  NARUTO_HIT_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/hit_w48_h47.png",3,100,5,20,5]  

  NARUTO_SKILL1_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/skill1_w48_h64.png",3,50,7,25,25]  
  NARUTO_SKILL1_COLLIDER_ANIMATIONS = [2,3,4]
  NARUTO_SKILL1_COLLIDER_DICTIONARY = {
    2:[[-NARUTO_WIDTH_RECT/2 + 30,-NARUTO_HEIGHT_RECT/2 - 20],[60,40]],
    3:[[-NARUTO_WIDTH_RECT/2 + 30,-NARUTO_HEIGHT_RECT/2 - 70],[60,40]],
    4:[[-NARUTO_WIDTH_RECT/2 + 30,-NARUTO_HEIGHT_RECT/2 - 80],[60,40]]
  }

  NARUTO_SKILL2_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/skill2_w64_h80.png",3,50,20,20,33]  
  NARUTO_SKILL2_COLLIDER_ANIMATIONS = []
  NARUTO_SKILL2_COLLIDER_DICTIONARY = {
  }
  NARUTO_SKILL3_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/skill3_w80_h48.png",3,50,13,50,5]  
  NARUTO_SKILL3_COLLIDER_ANIMATIONS = []
  NARUTO_SKILL3_COLLIDER_DICTIONARY = {
  }
  NARUTO_ENERGY_BALL_SPRITESHEET_SOURCE = ["Assets/Characters/Naruto/energy_ball_w55_h55.png",1.5,30,10,10,10] 
  NARUTO_ENERGY_BALL_SIZE = [50,50]
  NARUTO_ENERGY_BALL_SPEED = 40
  
  # sasuke character image source and props
  SASUKE_WIDTH_RECT = 60
  SASUKE_HEIGHT_RECT = 110
  SASUKE_IDLE_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/idle.png",3,50,7,7,5]# 0:source, 1:scale, 2:animation cooldown,3:offsetx,4: offsetx flip, 5:offsety
  SASUKE_MOVE_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/move.png",3,50,15,15,5]
  SASUKE_JUMP_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/jump.png",3,50,5,5,5]
  SASUKE_FALL_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/fall.png",3,50,5,5,5]
  SASUKE_ATTACK1_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/attack1.png",3,100,10,25,5]   
  SASUKE_ATTACK1_COLLIDER_ANIMATIONS = [2]
  SASUKE_ATTACK1_COLLIDER_DICTIONARY = {
    2:[[NARUTO_WIDTH_RECT*1.5,-NARUTO_HEIGHT_RECT/2 + 40],[60,35]]
  }
  SASUKE_ATTACK2_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/attack2.png",3,120,5,23,5]  
  SASUKE_ATTACK2_COLLIDER_ANIMATIONS = [3]
  SASUKE_ATTACK2_COLLIDER_DICTIONARY = {
    3:[[NARUTO_WIDTH_RECT*2,-NARUTO_HEIGHT_RECT/2 + 20],[100,35]]   # animation_index: [[pos relate character center x, pos relate character center y],[width,height]]
  }
  SASUKE_ATTACK3_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/attack3.png",3,120,5,23,5]  
  SASUKE_ATTACK3_COLLIDER_ANIMATIONS = [3]
  SASUKE_ATTACK3_COLLIDER_DICTIONARY = {
    3:[[NARUTO_WIDTH_RECT*1.75,-NARUTO_HEIGHT_RECT/2],[60,60]]
  }
  SASUKE_HIT_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/hit.png",3,150,5,20,5]  
  SASUKE_DASH_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/dash.png",3,40,10,25,5]  
  
  SASUKE_SKILL1_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/skill1.png",3,60,13,50,5]  
  SASUKE_SKILL1_COLLIDER_ANIMATIONS = []
  SASUKE_SKILL1_COLLIDER_DICTIONARY = {
  }
  SASUKE_ENERGY_BALL_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/thunder.png",1.5,30,10,10,10] 
  SASUKE_ENERGY_BALL_SIZE = [50,50]
  SASUKE_ENERGY_BALL_SPEED = 40
  
  SASUKE_SKILL2_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/skill2.png", 3, 50, 25, 30, 3]
  SASUKE_SKILL2_COLLIDER_ANIMATIONS = [10, 11, 12, 13, 14, 15]

  SASUKE_SKILL2_COLLIDER_DICTIONARY = {
      10: [[-SASUKE_WIDTH_RECT / 2 + 50, -SASUKE_WIDTH_RECT / 2 + 20], [80, 80]],
      11: [[-SASUKE_WIDTH_RECT / 2 + 50, -SASUKE_WIDTH_RECT / 2 + 20], [80, 80]],
      12: [[-SASUKE_WIDTH_RECT / 2 + 50, -SASUKE_WIDTH_RECT / 2 + 20], [80, 80]],
      13: [[-SASUKE_WIDTH_RECT / 2 + 50, -SASUKE_WIDTH_RECT / 2 + 20], [80, 80]],
      14: [[-SASUKE_WIDTH_RECT / 2 + 50, -SASUKE_WIDTH_RECT / 2 + 20], [80, 80]],
      15: [[-SASUKE_WIDTH_RECT / 2 + 50, -SASUKE_WIDTH_RECT / 2 + 20], [80, 80]]
  }
  
  SASUKE_SKILL3_SPRITESHEET_SOURCE = ["Assets/Characters/Sasuke/skill3.png", 3, 80, 95, 110, 20]
  SASUKE_SKILL3_COLLIDER_ANIMATIONS = [8, 9, 10, 11]

  SASUKE_SKILL3_COLLIDER_DICTIONARY = {
    8: [[-SASUKE_WIDTH_RECT / 2 - 180, -SASUKE_HEIGHT_RECT / 0.5 + 80], [1, 1]],
    9: [[-SASUKE_WIDTH_RECT / 2 - 180, -SASUKE_HEIGHT_RECT /  0.5 + 80], [1, 1]],
    10: [[-SASUKE_WIDTH_RECT / 2 - 180, -SASUKE_HEIGHT_RECT /  0.5+ 80], [1, 1]],
    11: [[-SASUKE_WIDTH_RECT / 2 - 180, -SASUKE_HEIGHT_RECT /  0.5 + 80], [1, 1]]
  }

  
  # rocklee character image source and props
  ROCKLEE_WIDTH_RECT = 60
  ROCKLEE_HEIGHT_RECT = 110
  ROCKLEE_IDLE_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/idle.png",3,70,7,7,5]# 0:source, 1:scale, 2:animation cooldown,3:offsetx,4: offsetx flip, 5:offsety
  ROCKLEE_MOVE_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/move.png",3,50,15,15,5]
  ROCKLEE_JUMP_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/jump.png",3,50,5,5,5]
  ROCKLEE_FALL_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/fall.png",3,50,5,5,5]
  ROCKLEE_ATTACK1_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/attack1.png",3,100,4,25,2]  
  ROCKLEE_ATTACK1_COLLIDER_ANIMATIONS = [3]
  ROCKLEE_ATTACK1_COLLIDER_DICTIONARY = {
    3:[[ROCKLEE_WIDTH_RECT/2,-ROCKLEE_HEIGHT_RECT/2 + 20],[60,35]]
  }
  ROCKLEE_ATTACK2_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/attack2.png",3,100,15,23,5]  
  ROCKLEE_ATTACK2_COLLIDER_ANIMATIONS = [3]
  ROCKLEE_ATTACK2_COLLIDER_DICTIONARY = {
    3:[[ROCKLEE_WIDTH_RECT/2,-ROCKLEE_HEIGHT_RECT/2 + 20],[62,35]]   # animation_index: [[pos relate character center x, pos relate character center y],[width,height]]
  }
  ROCKLEE_ATTACK3_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/attack3.png",3,100,15,20,30]  
  ROCKLEE_ATTACK3_COLLIDER_ANIMATIONS = [2]
  ROCKLEE_ATTACK3_COLLIDER_DICTIONARY = {
    2:[[ROCKLEE_WIDTH_RECT/2,-ROCKLEE_HEIGHT_RECT/2- 5],[60,35]]
  }

  ROCKLEE_HIT_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/hit.png",3,100,5,20,5]
  ROCKLEE_DASH_SPRITESHEET_SOURCE = ["Assets/Characters/RockLee/dash.png",3,40,10,25,5]  

  # sakura character image source and props
  SAKURA_WIDTH_RECT = 60
  SAKURA_HEIGHT_RECT = 110
  SAKURA_IDLE_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_idle_h49_w34.png", 3, 50, 7, 7,
                                    6]  # 0:source, 1:scale, 2:animation cooldown,3:offsetx,4: offsetx flip, 5:offsety
  SAKURA_MOVE_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_move_h48_w50.png", 3, 50, 15, 15, 5]
  SAKURA_JUMP_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_jump_h48_w34.png", 3, 50, 8, 6, 5]
  SAKURA_FALL_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_fall_h48_w40.png", 3, 50, 8, 6, 5]
  SAKURA_ATTACK1_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_Attack1_h48_w62.png", 3, 100, 15, 27, 3]
  SAKURA_ATTACK1_COLLIDER_ANIMATIONS = [3]
  SAKURA_ATTACK1_COLLIDER_DICTIONARY = {
    3: [[SAKURA_WIDTH_RECT / 2, -SAKURA_HEIGHT_RECT / 2 + 20], [60, 35]]
  }
  SAKURA_ATTACK2_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_Attack2_h49_w53.png", 3, 100, 15, 18, 9]
  SAKURA_ATTACK2_COLLIDER_ANIMATIONS = [3]
  SAKURA_ATTACK2_COLLIDER_DICTIONARY = {
    3: [[SAKURA_WIDTH_RECT / 2, -SAKURA_HEIGHT_RECT / 2 + 20], [62, 35]]
    # animation_index: [[pos relate character center x, pos relate character center y],[width,height]]
  }
  SAKURA_ATTACK3_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_Attack3_h50_w58.png", 3, 100, 10, 29, 8]
  SAKURA_ATTACK3_COLLIDER_ANIMATIONS = [2]
  SAKURA_ATTACK3_COLLIDER_DICTIONARY = {
    2: [[SAKURA_WIDTH_RECT / 2, -SAKURA_HEIGHT_RECT / 2 - 5], [60, 35]]
  }
  SAKURA_HIT_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_hit_h40_w39.png", 3, 50, 5, 20, 5]
  SAKURA_DASH_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_dash_h49_w34.png", 3, 40, 4, 10, 8]

  SAKURA_SKILL1_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_skill1_new_h64_w226.png", 3, 50, 93, 113, 17]
  SAKURA_SKILL1_COLLIDER_ANIMATIONS = []

  SAKURA_SKILL1_COLLIDER_DICTIONARY = {
  }

  SAKURA_SKILL2_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_skill2_h44_w74.png", 3, 50, 25, 30, 3]
  SAKURA_SKILL2_COLLIDER_ANIMATIONS = [10, 11, 12, 13, 14, 15]

  SAKURA_SKILL2_COLLIDER_DICTIONARY = {
      10: [[-SAKURA_WIDTH_RECT / 2 + 50, -SAKURA_HEIGHT_RECT / 2 + 20], [80, 80]],
      11: [[-SAKURA_WIDTH_RECT / 2 + 50, -SAKURA_HEIGHT_RECT / 2 + 20], [80, 80]],
      12: [[-SAKURA_WIDTH_RECT / 2 + 50, -SAKURA_HEIGHT_RECT / 2 + 20], [80, 80]],
      13: [[-SAKURA_WIDTH_RECT / 2 + 50, -SAKURA_HEIGHT_RECT / 2 + 20], [80, 80]],
      14: [[-SAKURA_WIDTH_RECT / 2 + 50, -SAKURA_HEIGHT_RECT / 2 + 20], [80, 80]],
      15: [[-SAKURA_WIDTH_RECT / 2 + 50, -SAKURA_HEIGHT_RECT / 2 + 20], [80, 80]]
  }

  SAKURA_SKILL3_SPRITESHEET_SOURCE = ["Assets/Characters/Sakura/sakura_skill3_h64_w226.png", 3, 50, 95, 110, 20]
  SAKURA_SKILL3_COLLIDER_ANIMATIONS = [8, 9, 10, 11]

  SAKURA_SKILL3_COLLIDER_DICTIONARY = {
    8: [[-SAKURA_WIDTH_RECT / 2 - 180, -SAKURA_HEIGHT_RECT / 2 + 80], [440, 50]],
    9: [[-SAKURA_WIDTH_RECT / 2 - 180, -SAKURA_HEIGHT_RECT / 2 + 80], [440, 50]],
    10: [[-SAKURA_WIDTH_RECT / 2 - 180, -SAKURA_HEIGHT_RECT / 2 + 80], [440, 50]],
    11: [[-SAKURA_WIDTH_RECT / 2 - 180, -SAKURA_HEIGHT_RECT / 2 + 80], [440, 50]]
  }

    #SFX
  #Naruto
  NARUTO_MOVE_SFX = ["Assets/SFX/NarutoSFX/move.wav",True] # source, loop
  NARUTO_JUMP_SFX = ["Assets/SFX/NarutoSFX/jump.wav",False]
  NARUTO_ATTACK1_SFX = ["Assets/SFX/NarutoSFX/nomal_attack_1.wav",False]
  NARUTO_ATTACK2_SFX = ["Assets/SFX/NarutoSFX/nomal_attack_2.wav",False]
  NARUTO_ATTACK3_SFX = ["Assets/SFX/NarutoSFX/nomal_attack_3.wav",False]
  NARUTO_SKILL1_SFX = ["Assets/SFX/NarutoSFX/skill_1.wav",False]
  NARUTO_SKILL2_SFX = ["Assets/SFX/NarutoSFX/skill_2.wav",False]
  NARUTO_SKILL3_SFX = ["Assets/SFX/NarutoSFX/skill_3.wav",False]
  NARUTO_WIN_SFX = ["Assets/SFX/NarutoSFX/Win.wav",False]
  NARUTO_DEATH_SFX = ["Assets/SFX/NarutoSFX/death.wav",False]
  NARUTO_HIT_SFX = ["Assets/SFX/NarutoSFX/hit.wav",False]



  # keyboard player1
  LEFT1 = pygame.K_a
  RIGHT1 = pygame.K_d
  UP1 = pygame.K_w
  DOWN1 = pygame.K_s
  NOMALATTACK1 = pygame.K_j
  SKILL1_1 = pygame.K_u
  SKILL2_1 = pygame.K_i
  SKILL3_1 = pygame.K_o
  DASH1 = pygame.K_l

  # keyboad player2
  LEFT2 = pygame.K_LEFT
  RIGHT2 = pygame.K_RIGHT
  UP2 = pygame.K_UP
  DOWN2 = pygame.K_DOWN
  NOMALATTACK2 = pygame.K_KP0
  SKILL1_2 = pygame.K_KP1
  SKILL2_2 = pygame.K_KP2
  SKILL3_2 = pygame.K_KP3
  DASH2 = pygame.K_KP6

  #base attribute
  GRAVITY = 2
  BASE_SPEED = 10
  BASE_JUMP_FORCE = 35
  IDLE_SPEED_MODIFIER = 0
  MOVE_SPEED_MODIFIER = 1
  JUMP_FORCE_MODIFIER = 1
  ZERO_FORCE_MODIFIER = 0
  BASE_HEALTH = 300
  BASE_MANA = 100
  TIME_RESET_ATTACK_COMBO = 2
  DASH_DURATION = 350  
  DASH_SPEED = 20     
  DASH_COOLDOWN = 750 


  

