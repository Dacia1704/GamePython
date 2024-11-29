import pygame
from Scripts.game_constants import GameConstants
from Scripts.Scene.scenebase import ScreenBase
from Scripts.Audio.audio_manager import AudioManager
import json
class MainMenu(ScreenBase):
	def __init__(self,screen):
		super().__init__(screen)
		self.font_black_30 = pygame.font.Font(GameConstants.ROBOTO_BLACK_1[0], GameConstants.ROBOTO_BLACK_1[1])
		self.font_game_name = pygame.font.Font(GameConstants.PROTESTREVOLUTION_REGULAR_1[0], GameConstants.PROTESTREVOLUTION_REGULAR_1[1])

		button_image_raw = pygame.image.load(GameConstants.RAW_BUTTON_IMAGE[0]).convert_alpha()
		button_width = button_image_raw.get_width()
		button_height = button_image_raw.get_height()
		self.button_image = pygame.transform.scale(button_image_raw,(button_width * GameConstants.RAW_BUTTON_IMAGE[1], button_height * GameConstants.RAW_BUTTON_IMAGE[1]))


		self.play_button_rect = pygame.Rect(GameConstants.SCREEN_WIDTH/2 - button_width/2, GameConstants.SCREEN_HEIGHT/2 -button_height -10 , button_width, button_height)
		self.setting_button_rect = pygame.Rect(GameConstants.SCREEN_WIDTH/2 - button_width/2, GameConstants.SCREEN_HEIGHT/2 , button_width, button_height)
		self.quit_button_rect = pygame.Rect(GameConstants.SCREEN_WIDTH/2 - button_width/2, GameConstants.SCREEN_HEIGHT/2 +button_height +10 , button_width, button_height)
		self.back_ground = pygame.transform.scale( pygame.image.load(GameConstants.RIVER_BG_IMAGE_SOURCE).convert_alpha(),(GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
		self.i_love_ptit_back_ground = pygame.transform.scale( pygame.image.load(GameConstants.I_LOVE_PTIT_BG_IMAGE_SOURCE).convert_alpha(),(GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))

		self.button_pressed = None

		self.main_menu_bgm = self.setup_bgm("main_menu",GameConstants.MAIN_MENU_BGM[0])

		self.bgm_volumn = 100
		self.vfx_volumn = 100
		self.load_volume_settings()
		AudioManager.get_instance().set_music_volume(self.bgm_volumn/100)
		AudioManager.get_instance().set_sfx_volume(self.sfx_volumn/100)

		self.start_time = pygame.time.get_ticks()
		self.time_show_i_love_ptit = 3000



	def handle_events(self, events):
		for event in events:
				if event.type == pygame.QUIT:
						return "QUIT"
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Kiểm tra nhấn chuột trái
						if self.play_button_rect.collidepoint(event.pos):
								self.button_pressed = "PLAY"
						elif self.quit_button_rect.collidepoint(event.pos):
								self.button_pressed = "QUIT"
						elif self.setting_button_rect.collidepoint(event.pos):
								self.button_pressed = "SETTING"

				if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Nhả chuột
						if self.button_pressed == "PLAY":
								self.next_scene = "CHARACTER_SELECTION"  # Chuyển đến scene chọn nhân vật
								AudioManager.get_instance().stop_music("main_menu")
						elif self.button_pressed == "SETTING":
							self.next_scene = "SETTING"
						elif self.button_pressed == "QUIT":
								return "QUIT"
						self.button_pressed = None

	def update(self):
		if pygame.time.get_ticks() - self.start_time < self.time_show_i_love_ptit:
			self.screen.blit(self.i_love_ptit_back_ground, (0, 0))
		else:
			self.screen.blit(self.back_ground, (0, 0))

			# Vẽ tên game
			self.draw_text_in_center_rect(
				"INFINITY FIGHTER", self.font_game_name, (255, 255, 255), self.screen.get_rect(), [0, -200]
			)

			# Vẽ nút Play
			self.screen.blit(self.button_image, self.play_button_rect)
			if self.button_pressed == "PLAY":
				self.draw_button_overlay(self.play_button_rect)
			self.draw_text_in_center_rect("PLAY", self.font_black_30, (255, 255, 255), self.play_button_rect)

			# Vẽ nút Setting
			self.screen.blit(self.button_image, self.setting_button_rect)
			if self.button_pressed == "SETTING":
				self.draw_button_overlay(self.setting_button_rect)
			self.draw_text_in_center_rect("SETTING", self.font_black_30, (255, 255, 255), self.setting_button_rect)

			# Vẽ nút Quit
			self.screen.blit(self.button_image, self.quit_button_rect)
			if self.button_pressed == "QUIT":
				self.draw_button_overlay(self.quit_button_rect)
			self.draw_text_in_center_rect("QUIT", self.font_black_30, (255, 255, 255), self.quit_button_rect)

			# Kiểm tra chuyển cảnh
			if self.next_scene == "CHARACTER_SELECTION":
				return "CHARACTER_SELECTION"

		
	def start(self):
		super().start()
		AudioManager.get_instance().play_music(self.main_menu_bgm )

	def exit(self):
		super().exit()
		AudioManager.get_instance().stop_music(self.main_menu_bgm )
		
	def load_volume_settings(self, filename="volume_settings.json"):
		try:
			with open(filename, "r") as file:
				data = json.load(file)
				self.bgm_volumn =  data.get("bgm_volume", 100)
				self.sfx_volumn =  data.get("sfx_volume", 100)
			print(f"Tải dữ liệu thành công từ {filename} {self.bgm_volumn} {self.sfx_volumn}")
		except FileNotFoundError:
			print(f"Không tìm thấy tệp {filename}. Sử dụng giá trị mặc định.")
		except json.JSONDecodeError as e:
			print(f"Lỗi khi đọc tệp JSON: {e}")
		except IOError as e:
			print(f"Lỗi khi tải dữ liệu: {e}")