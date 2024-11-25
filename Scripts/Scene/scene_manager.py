from Scripts.Scene.game_scene import GameScene
from Scripts.Scene.main_menu import MainMenu
from Scripts.Audio.audio_manager import AudioManager
from Scripts.Scene.setting_scene import SettingGame
import pygame
class SceneManager:
	def __init__(self,screen):
		self.screen = screen
		self.scenes = {
				"MAIN_MENU": MainMenu(screen),
				"GAME": GameScene(screen),
				"SETTING": SettingGame(screen),
		}
		self.current_scene = self.scenes["MAIN_MENU"]
		self.current_scene.start()
		self.next_scene_name = None  # Tên của cảnh tiếp theo
		self.transition_time = None  # Thời gian bắt đầu chuyển cảnh

	def change_scene(self, scene_name):
		if scene_name in self.scenes:
				self.current_scene.exit()
				self.current_scene = self.scenes[scene_name]
				self.current_scene.start()

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

	def update(self):
		if self.transition_time is not None:
			current_time = pygame.time.get_ticks()
			# Nếu đã qua 1 giây, thực hiện chuyển cảnh
			if current_time - self.transition_time >= 500:
					self.change_scene(self.next_scene_name)
					self.next_scene_name = None
					self.transition_time = None
		# Cập nhật cảnh hiện tại bình thường
		self.current_scene.update()