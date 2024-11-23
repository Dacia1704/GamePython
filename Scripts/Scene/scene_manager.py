from Scripts.Scene.game_scene import GameScene
from Scripts.Scene.main_menu import MainMenu
import pygame
class SceneManager:
	def __init__(self,screen):
		self.screen = screen
		self.scenes = {
				"MAIN_MENU": MainMenu(screen),
				"GAME": GameScene(screen),
		}
		self.current_scene = self.scenes["MAIN_MENU"]
		self.next_scene_name = None  # Tên của cảnh tiếp theo
		self.transition_time = None  # Thời gian bắt đầu chuyển cảnh

	def change_scene(self, scene_name):
		if scene_name in self.scenes:
				self.current_scene = self.scenes[scene_name]

	def handle_events(self, events):  # return to running result in main
		result = self.current_scene.handle_events(events)
		if result == "QUIT":
			return False
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