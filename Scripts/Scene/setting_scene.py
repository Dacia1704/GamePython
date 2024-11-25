import pygame
from Scripts.game_constants import GameConstants
from Scripts.Scene.scenebase import ScreenBase
from Scripts.Audio.audio_manager import AudioManager


class SettingGame(ScreenBase):
    def __init__(self, screen):
        super().__init__(screen)
        # Phông chữ cho tiêu đề "Setting"
        self.font_title = pygame.font.Font(GameConstants.PROTESTREVOLUTION_REGULAR_1[0],
                                           GameConstants.PROTESTREVOLUTION_REGULAR_1[1] + 10)

        # Phông chữ cho các phần khác
        self.font_black_30 = pygame.font.Font(GameConstants.ROBOTO_BLACK_1[0], GameConstants.ROBOTO_BLACK_1[1])

        button_image_raw = pygame.image.load(GameConstants.RAW_BUTTON_IMAGE[0]).convert_alpha()
        button_width = button_image_raw.get_width()
        button_height = button_image_raw.get_height()
        self.button_image = pygame.transform.scale(button_image_raw,
                                                   (button_width * GameConstants.RAW_BUTTON_IMAGE[1],
                                                    button_height * GameConstants.RAW_BUTTON_IMAGE[1]))

        # Vị trí và kích thước các thanh trượt
        self.bgm_slider_rect = pygame.Rect(GameConstants.SCREEN_WIDTH / 2 - 150, GameConstants.SCREEN_HEIGHT / 2 - 50,
                                           300, 10)
        self.sfx_slider_rect = pygame.Rect(GameConstants.SCREEN_WIDTH / 2 - 150, GameConstants.SCREEN_HEIGHT / 2 + 50,
                                           300, 10)

        self.bgm_value = 100  # Giá trị âm lượng BGM ban đầu (tính theo phần trăm)
        self.sfx_value = 100  # Giá trị âm lượng SFX ban đầu (tính theo phần trăm)

        self.slider_color = (200, 200, 200)
        self.button_color = (255, 255, 255)

        # Khởi tạo nhạc nền cài đặt
        self.main_menu_bgm = self.setup_bgm("settings", GameConstants.MAIN_MENU_BGM[0])

        # Tải hình nền cho màn hình Setting
        self.back_ground = pygame.transform.scale(
            pygame.image.load(GameConstants.RIVER_BG_IMAGE_SOURCE).convert_alpha(),
            (GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT)
        )

        # Khởi tạo nút "Back"
        self.back_button_rect = pygame.Rect(GameConstants.SCREEN_WIDTH / 2 - button_width / 2,
                                            GameConstants.SCREEN_HEIGHT - 150,
                                            button_width, button_height)

        # Lấy instance AudioManager
        self.audio_manager = AudioManager.get_instance()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Nhấn chuột trái
                if self.bgm_slider_rect.collidepoint(event.pos):
                    self.bgm_value = self.get_slider_value(event.pos, self.bgm_slider_rect)
                elif self.sfx_slider_rect.collidepoint(event.pos):
                    self.sfx_value = self.get_slider_value(event.pos, self.sfx_slider_rect)
                elif self.back_button_rect.collidepoint(event.pos):
                    return "MAIN_MENU"  # Trở về màn hình chính

            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:  # Kéo thanh trượt
                    if self.bgm_slider_rect.collidepoint(event.pos):
                        self.bgm_value = self.get_slider_value(event.pos, self.bgm_slider_rect)
                    elif self.sfx_slider_rect.collidepoint(event.pos):
                        self.sfx_value = self.get_slider_value(event.pos, self.sfx_slider_rect)

        # Cập nhật âm lượng
        self.audio_manager.set_music_volume(self.bgm_value / 100)
        self.audio_manager.set_sfx_volume(self.sfx_value / 100)

    def update(self):
        self.screen.blit(self.back_ground, (0, 0))

        # Vẽ tiêu đề màn hình "Setting"
        self.draw_text_in_center_rect("SETTING", self.font_title, (255, 255, 255), self.screen.get_rect(), [0, -200])

        # Vẽ thanh trượt BGM
        pygame.draw.rect(self.screen, self.slider_color, self.bgm_slider_rect)
        pygame.draw.circle(self.screen, (255, 255, 255),
                           (self.bgm_slider_rect.x + self.bgm_value * 3, self.bgm_slider_rect.centery), 10)

        # Vẽ thanh trượt SFX
        pygame.draw.rect(self.screen, self.slider_color, self.sfx_slider_rect)
        pygame.draw.circle(self.screen, (255, 255, 255),
                           (self.sfx_slider_rect.x + self.sfx_value * 3, self.sfx_slider_rect.centery), 10)

        # Hiển thị giá trị âm lượng
        self.draw_text_in_center_rect(f"BGM Volume: {self.bgm_value}%", self.font_black_30, (255, 255, 255),
                                      self.bgm_slider_rect, [0, -30])
        self.draw_text_in_center_rect(f"SFX Volume: {self.sfx_value}%", self.font_black_30, (255, 255, 255),
                                      self.sfx_slider_rect, [0, -30])
        # Vẽ nút "Back"
        self.screen.blit(self.button_image, self.back_button_rect)
        self.draw_text_in_center_rect("BACK", self.font_black_30, (255, 255, 255), self.back_button_rect)
    def get_slider_value(self, mouse_pos, slider_rect):
        # Tính giá trị thanh trượt dựa trên vị trí chuột
        if slider_rect.collidepoint(mouse_pos):
            return min(max(0, (mouse_pos[0] - slider_rect.x) // 3), 100)
        return self.bgm_value  # Trả về giá trị mặc định nếu không nằm trong thanh trượt

    def start(self):
        super().start()
        # Chạy nhạc nền cho màn hình cài đặt
        AudioManager.get_instance().play_music(self.main_menu_bgm)

    def exit(self):
        super().exit()
        # Dừng nhạc nền khi rời khỏi màn hình cài đặt
        AudioManager.get_instance().stop_music(self.main_menu_bgm)
