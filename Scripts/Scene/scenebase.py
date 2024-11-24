import pygame
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
class ScreenBase:
	def __init__(self,screen):
		self.next_scene = None
		self.screen = screen
	def draw_text_in_center_rect(self,text,font,text_color,rect_parent,offset = [0,0]):
		render_text = font.render(text, True, text_color)
		render_text_rect = render_text.get_rect(center=rect_parent.center)
		render_text_rect_with_offset = pygame.Rect((render_text_rect.x + offset[0],render_text_rect.y + offset[1],render_text_rect.width,render_text_rect.height))
		self.screen.blit(render_text, render_text_rect_with_offset)

	def draw_button_overlay(self, rect):
			overlay = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
			overlay.fill((0, 0, 0, 100))
			self.screen.blit(overlay, rect.topleft)

	def start(self):
		#print("start")
		pass
	def exit(self):
		#print("exit")
		pass

	def setup_bgm(self,name,path):
		AudioManager.get_instance().load_music(name,path)
		return name