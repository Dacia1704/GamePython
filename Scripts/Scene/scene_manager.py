from Scripts.Scene.game_scene import GameScene
from Scripts.Scene.main_menu import MainMenu
from Scripts.Scene.CharacterSelection import CharacterSelectionScene
from Scripts.Audio.audio_manager import AudioManager
from Scripts.Scene.setting_scene import SettingGame
import pygame
class SceneManager:
	def __init__(self,screen):
		self.screen = screen
		self.scenes = {
				"MAIN_MENU": MainMenu(screen),
				"CHARACTER_SELECTION": CharacterSelectionScene(screen),
				"SETTING": SettingGame(screen),
		}
		self.current_scene = self.scenes["MAIN_MENU"]
		self.current_scene.start()
		self.next_scene_name = None  # Tên của cảnh tiếp theo
		self.transition_time = None  # Thời gian bắt đầu chuyển cảnh

	def update(self):
		if self.transition_time is not None:
			current_time = pygame.time.get_ticks()
			if current_time - self.transition_time >= 500:
				self.change_scene(self.next_scene_name)
				self.next_scene_name = None
				self.transition_time = None
		elif self.current_scene.next_scene:
			self.next_scene_name = self.current_scene.next_scene
			self.transition_time = pygame.time.get_ticks()	
		self.current_scene.update()

	def handle_events(self, events):  # return to running result in main
		result = self.current_scene.handle_events(events)
		if result == "QUIT":
			return False
		# Kiểm tra nếu cảnh hiện tại là SettingGame và người dùng chọn quay lại Main Menu
		if isinstance(self.current_scene, SettingGame) and result == "MAIN_MENU":
			self.change_scene("MAIN_MENU")  # Chuyển về Main Menu
		if self.current_scene.next_scene:
			self.next_scene_name = self.current_scene.next_scene
			self.transition_time = pygame.time.get_ticks()  # Lưu thời gian bắt đầu
			self.current_scene.next_scene = None
		return True

	def change_scene(self, scene_name):
			# Thêm điều kiện để tạo lại GAME scene nếu cần
			if scene_name == "GAME" and isinstance(self.current_scene, CharacterSelectionScene):
				selected_characters = self.current_scene.selected_characters
				self.scenes["GAME"] = GameScene(self.screen, selected_characters=selected_characters)

			# Chuyển đổi cảnh
			self.current_scene.exit()
			self.current_scene = self.scenes[scene_name]
			self.current_scene.start()