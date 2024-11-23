import pygame
from Scripts.game_constants import GameConstants
from Scripts.Input.game_input import GameInput
from Scripts.PlayerCharacter.Naruto.naruto_character import NarutoCharacter
from Scripts.PlayerCharacter.Sasuke.sasuke_character import SasukeCharacter
from Scripts.PlayerCharacter.RockLee.rocklee_character import RockLeeCharacter
from Scripts.PlayerCharacter.Sakura.sakura_character import SakuraCharacter
from Scripts.Scene.scenebase import ScreenBase
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
		self.player2 = NarutoCharacter(2,1000,GameConstants.SCREEN_HEIGHT-GameConstants.GROUND_Y,screen,None)
		self.player1 = SakuraCharacter(1,200,GameConstants.SCREEN_HEIGHT-GameConstants.GROUND_Y,screen,self.player2)
		self.player2.target = self.player1
		self.player1.start()
		self.player2.start()

	def handle_events(self, events):
		for event in events:
				if event.type == pygame.QUIT:
						return "QUIT"
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
						self.next_scene = "MAIN_MENU"

	def update(self):
		#draw bg
		self.screen.blit(self.back_round_battle[0], (0, 0))

		#input update
		GameInput.get_instance().update()

		#player
		self.player1.update()
		self.player2.update()