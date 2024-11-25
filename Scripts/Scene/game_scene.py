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
    def __init__(self, screen, selected_characters):
        super().__init__(screen)
        self.screen = screen
        self.selected_characters = selected_characters
        self.characters = [
            ("Naruto", NarutoCharacter),
            ("Sasuke", SasukeCharacter),
            ("RockLee", RockLeeCharacter),
            ("Sakura", SakuraCharacter),
        ]
        self.init_players()
        # Load background images
        self.back_round_battle = [
            pygame.transform.scale(
                pygame.image.load(GameConstants.HOKAGE_STATE_BG_IMAGE_SOURCE).convert_alpha(),
                (GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT),
            ),
            pygame.transform.scale(
                pygame.image.load(GameConstants.SUMMER_VILLAGE_BG_IMAGE_SOURCE).convert_alpha(),
                (GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT),
            ),
            pygame.transform.scale(
                pygame.image.load(GameConstants.WINTER_VILLAGE_BG_IMAGE_SOURCE).convert_alpha(),
                (GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT),
            ),
        ]

        

        # Define colors
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0,255,0)
        self.ORANGE = (255,165,0)
        self.GRAY = (211,211,211)
    def init_players(self):
        # Lấy lớp nhân vật được chọn
        player1_class = self.characters[self.selected_characters[1]][1]
        player2_class = self.characters[self.selected_characters[2]][1]

        # Khởi tạo nhân vật
        self.player1 = player1_class(
            1, 200, GameConstants.SCREEN_HEIGHT - GameConstants.GROUND_Y, self.screen, None
        )
        self.player2 = player2_class(
            2, 600, GameConstants.SCREEN_HEIGHT - GameConstants.GROUND_Y, self.screen, None
        )

        # Gán mục tiêu
        self.player1.target = self.player2
        self.player2.target = self.player1  # Đảm bảo player2 có target

        # Khởi động trạng thái của nhân vật
        self.player1.start()
        self.player2.start()

        # Thiết lập âm thanh
        self.battle_3_bgm = self.setup_bgm("battle_3", GameConstants.BATTLE_3_BGM[0])

    # Các phương thức bạn đề cập đặt tại đây:
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
        # pygame.draw.rect(self.screen, self.WHITE, (x - 2, y - 2, 204, 19))
        # pygame.draw.rect(self.screen, self.BLUE, (x, y, 200 * ratio, 15))
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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        self.next_scene = "MAIN_MENU"

    def update(self):
        #draw bg
        self.screen.blit(self.back_round_battle[0], (0, 0))

        # draw health and mana bars
        self.draw_health_bar(self.player1.health, 20, 20,1)
        self.draw_health_bar(self.player2.health, GameConstants.SCREEN_WIDTH-20, 20,2)
        self.draw_mana_bar(self.player1.mana, 20, 52,1)
        self.draw_mana_bar(self.player2.mana, GameConstants.SCREEN_WIDTH-20, 52,2)

        #input update
        GameInput.get_instance().update()

        #player
        self.player1.update()
        self.player2.update()
    def start(self):
        super().start()
        AudioManager.get_instance().play_music(self.battle_3_bgm)

    def exit(self):
        super().exit()
        AudioManager.get_instance().stop_music(self.battle_3_bgm)