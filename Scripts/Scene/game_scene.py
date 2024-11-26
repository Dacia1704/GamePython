import pygame
from Scripts.game_constants import GameConstants
from Scripts.Input.game_input import GameInput
from Scripts.PlayerCharacter.Naruto.naruto_character import NarutoCharacter
from Scripts.PlayerCharacter.Sasuke.sasuke_character import SasukeCharacter
from Scripts.PlayerCharacter.RockLee.rocklee_character import RockLeeCharacter
from Scripts.PlayerCharacter.Sakura.sakura_character import SakuraCharacter
from Scripts.Scene.scenebase import ScreenBase
from Scripts.Audio.audio_manager import AudioManager
class GameScene(ScreenBase):
	def __init__(self,screen):
		super().__init__(screen)



		#load bg images
		self.back_round_battle = [
				pygame.transform.scale( pygame.image.load(GameConstants.HOKAGE_STATE_BG_IMAGE_SOURCE).convert_alpha(),(GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT)),
				pygame.transform.scale( pygame.image.load(GameConstants.SUMMER_VILLAGE_BG_IMAGE_SOURCE).convert_alpha(),(GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT)),
				pygame.transform.scale( pygame.image.load(GameConstants.WINTER_VILLAGE_BG_IMAGE_SOURCE).convert_alpha(),(GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT)),
		]



		#player
		self.battle_finish = False
		self.player2 = NarutoCharacter(self,2,1000,GameConstants.SCREEN_HEIGHT-GameConstants.GROUND_Y,screen,None)
		self.player1 = SakuraCharacter(self,1,200,GameConstants.SCREEN_HEIGHT-GameConstants.GROUND_Y,screen,self.player2)
		self.player2.target = self.player1
		self.player1.start()
		self.player2.start()

		self.battle_3_bgm = self.setup_bgm("battle_3",GameConstants.BATTLE_3_BGM[0])

		# define colours
		self.RED = (255, 0, 0)
		self.YELLOW = (255, 255, 0)
		self.WHITE = (255, 255, 255)
		self.BLUE = (0, 0, 255)
		self.BLACK = (0, 0, 0)
		self.GREEN = (0,255,0)
		self.ORANGE = (255,165,0)
		self.GRAY = (211,211,211)

		
		self.font_black_20 = pygame.font.Font(GameConstants.ROBOTO_BLACK_3[0], GameConstants.ROBOTO_BLACK_3[1])
		self.font_game_name = pygame.font.Font(GameConstants.PROTESTREVOLUTION_REGULAR_1[0], GameConstants.PROTESTREVOLUTION_REGULAR_1[1])

		button_image_raw = pygame.image.load(GameConstants.RAW_BUTTON_IMAGE[0]).convert_alpha()
		button_width = button_image_raw.get_width() * GameConstants.RAW_BUTTON_IMAGE[1] -10
		button_height = button_image_raw.get_height() * GameConstants.RAW_BUTTON_IMAGE[1] -10
		self.button_image = pygame.transform.scale(button_image_raw,(button_width, button_height))

		self.button_pressed = None

		self.play_again_button_rect = pygame.Rect(GameConstants.SCREEN_WIDTH/2 - button_width  -10, GameConstants.SCREEN_HEIGHT/2 +5, button_width, button_height)
		self.back_to_menu_button_rect = pygame.Rect(GameConstants.SCREEN_WIDTH/2  + 10 , GameConstants.SCREEN_HEIGHT/2 +5, button_width, button_height)

	def update(self):
		#draw bg
		self.screen.blit(self.back_round_battle[0], (0, 0))

		
		# draw health and mana bars
		self.draw_health_bar(self.player1.health, 20, 20,1)
		self.draw_health_bar(self.player2.health, GameConstants.SCREEN_WIDTH-20, 20,2)
		self.draw_mana_bar(self.player1.mana, 20, 52,1)
		self.draw_mana_bar(self.player2.mana, GameConstants.SCREEN_WIDTH-20, 52,2)
		if not self.battle_finish:
			#input update
			GameInput.get_instance().update()
			#player
			self.player1.update()
			self.player2.update()
		else:
			#player
			self.player1.update()
			self.player2.update()
			self.draw_battle_end()

	def start(self):
		super().start()
		AudioManager.get_instance().play_music(self.battle_3_bgm)

	def exit(self):
		super().exit()
		AudioManager.get_instance().stop_music(self.battle_3_bgm)
	def draw_health_bar(self, health, x, y,player_id):   # player1: thì truyền góc trái trên, player2: truyền góc phải trên
		ratio = health / 300
		width = 500
		height = 30
		hp_color =None
		if(ratio > 0.5):
			hp_color = self.GREEN
		elif(ratio >0.15):
			hp_color = self.ORANGE
		else:
			hp_color = self.RED
		if(player_id == 1):
			pygame.draw.rect(self.screen, self.BLACK, (x - 2, y - 2, width+4, height+4))
			pygame.draw.rect(self.screen, self.GRAY, (x, y, width, height))
			pygame.draw.rect(self.screen, hp_color, (x, y, width * ratio, height))
		else:
			pygame.draw.rect(self.screen, self.BLACK, (x - 2 -width, y - 2, width+4, height+4))
			pygame.draw.rect(self.screen, self.GRAY, (x -width, y, width, height))
			pygame.draw.rect(self.screen, hp_color, (x - width * ratio, y, width * ratio, height))

	def draw_mana_bar(self, mana, x, y,player_id):
		ratio = mana / 100
		width = 300
		height = 15
		if(player_id == 1):
			pygame.draw.rect(self.screen, self.BLACK, (x - 2, y - 2, width+4, height+4))
			pygame.draw.rect(self.screen, self.GRAY, (x, y, width, height))
			pygame.draw.rect(self.screen, self.BLUE, (x, y, width * ratio, height))
		else:
			pygame.draw.rect(self.screen, self.BLACK, (x - 2 -width, y - 2, width+4, height+4))
			pygame.draw.rect(self.screen, self.GRAY, (x -width, y, width, height))
			pygame.draw.rect(self.screen, self.BLUE, (x - width * ratio, y, width * ratio, height))

	def handle_events(self, events):
		for event in events:
				if event.type == pygame.QUIT:
						return "QUIT"
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Kiểm tra nhấn chuột trái
						if self.play_again_button_rect.collidepoint(event.pos):
								self.button_pressed = "PLAY_AGAIN"
						elif self.back_to_menu_button_rect.collidepoint(event.pos):
								self.button_pressed = "BACK"

				if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					if self.play_again_button_rect.collidepoint(event.pos):
							self.button_pressed = "PLAY_AGAIN"
							# self.next_scene= ""
					elif self.back_to_menu_button_rect.collidepoint(event.pos):
							self.button_pressed = "BACK"
							self.next_scene = "MAIN_MENU"
					self.button_pressed = None

	def draw_battle_end(self):
		overlay = pygame.Surface((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT), pygame.SRCALPHA)
		overlay.fill((0, 0, 0, 100))
		self.screen.blit(overlay, (0,0))



		self.draw_text_in_center_rect("VICTORY",self.font_game_name,(255,255,0),self.screen.get_rect(),[0,-50])

		# Vẽ nút Play
		self.screen.blit(self.button_image,self.play_again_button_rect)
		if self.button_pressed == "PLAY_AGAIN":
				self.draw_button_overlay(self.play_again_button_rect)
		self.draw_text_in_center_rect("PLAY AGAIN",self.font_black_20,(255,255,255),self.play_again_button_rect)

		# Vẽ nút Setting
		self.screen.blit(self.button_image,self.back_to_menu_button_rect)
		if self.button_pressed == "BACK":
				self.draw_button_overlay(self.back_to_menu_button_rect)
		self.draw_text_in_center_rect("BACK",self.font_black_20,(255,255,255),self.back_to_menu_button_rect)