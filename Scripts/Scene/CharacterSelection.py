import pygame
from Scripts.Scene.scenebase import ScreenBase
from Scripts.PlayerCharacter.Naruto.naruto_character import NarutoCharacter
from Scripts.PlayerCharacter.Sasuke.sasuke_character import SasukeCharacter
from Scripts.PlayerCharacter.RockLee.rocklee_character import RockLeeCharacter
from Scripts.PlayerCharacter.Sakura.sakura_character import SakuraCharacter
from Scripts.game_constants import GameConstants


class CharacterSelectionScene(ScreenBase):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(None, 50)
        self.characters = [
            ("Naruto", NarutoCharacter),
            ("Sasuke", SasukeCharacter),
            ("RockLee", RockLeeCharacter),
            ("Sakura", SakuraCharacter),
        ]
        self.character_images = [
            pygame.image.load("Assets/AvaCha/naruto.png"),
            pygame.image.load("Assets/AvaCha/sasuke.png"),
            pygame.image.load("Assets/AvaCha/rocklee.png"),
            pygame.image.load("Assets/AvaCha/sakura.png"),
        ]
        self.selected_character = None
        self.current_player = 1
        self.selected_characters = {}
        self.play_button = pygame.Rect(
            GameConstants.SCREEN_WIDTH // 2 - 75, 600, 150, 50
        )
        self.back_button = pygame.Rect(50, 50, 100, 50)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Xử lý chọn nhân vật
                for idx, char_image in enumerate(self.character_images):
                    rect = pygame.Rect(
                        GameConstants.SCREEN_WIDTH // 2 - 75 + (idx - 2) * 150,
                        400,
                        150,
                        150,
                    )
                    if rect.collidepoint(event.pos):
                        self.selected_characters[self.current_player] = idx

                        if self.current_player == 2:  # Đã chọn cho player 2
                            self.selected_character = idx
                        else:
                            self.current_player = 2

                # Nút "Play" để xác nhận
                if self.play_button.collidepoint(event.pos):
                    if len(self.selected_characters) == 2:
                        self.next_scene = "GAME"

                # Nút "Back" để quay lại
                if self.back_button.collidepoint(event.pos):
                    self.next_scene = "MAIN_MENU"
            # Quay lại người chơi trước bằng phím ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.current_player == 2:
                    self.current_player = 1
                    del self.selected_characters[2]

    def update(self):
        self.screen.fill((0, 0, 0))  # Xóa màn hình

        # Tiêu đề
        title_text = f"Player {self.current_player} "
        title_surface = self.font.render(title_text, True, (255, 255, 255))
        self.screen.blit(
            title_surface, (GameConstants.SCREEN_WIDTH // 2 - title_surface.get_width() // 2, 50)
        )

        # Hiển thị nhân vật đã chọn
        if 1 in self.selected_characters:
            chosen_text = f"Player 1: {self.characters[self.selected_characters[1]][0]}"
            chosen_surface = self.font.render(chosen_text, True, (255, 255, 255))
            self.screen.blit(
                chosen_surface,
                (GameConstants.SCREEN_WIDTH // 2 - chosen_surface.get_width() // 2, 150),
            )

            # Hiển thị ảnh nhỏ của Player 1
            thumbnail = pygame.transform.scale(
                self.character_images[self.selected_characters[1]], (50, 50)
            )
            self.screen.blit(thumbnail, (GameConstants.SCREEN_WIDTH // 2 + 200, 150))

        if 2 in self.selected_characters:
            chosen_text = f"Player 2: {self.characters[self.selected_characters[2]][0]}"
            chosen_surface = self.font.render(chosen_text, True, (255, 255, 255))
            self.screen.blit(
                chosen_surface,
                (GameConstants.SCREEN_WIDTH // 2 - chosen_surface.get_width() // 2, 200),
            )

            # Hiển thị ảnh nhỏ của Player 2
            thumbnail = pygame.transform.scale(
                self.character_images[self.selected_characters[2]], (50, 50)
            )
            self.screen.blit(thumbnail, (GameConstants.SCREEN_WIDTH // 2 + 200, 200))

        # Vẽ danh sách nhân vật
        for idx, char_image in enumerate(self.character_images):
            rect = pygame.Rect(
                GameConstants.SCREEN_WIDTH // 2 - 75 + (idx - 2) * 150, 400, 150, 150
            )
            self.screen.blit(pygame.transform.scale(char_image, (150, 150)), rect)

        # Vẽ nút "Play"
        if len(self.selected_characters) == 2:
            pygame.draw.rect(self.screen, (0, 255, 0), self.play_button)
            play_text = self.font.render("Play", True, (0, 0, 0))
            self.screen.blit(
                play_text,
                (
                    self.play_button.x + self.play_button.width // 2 - play_text.get_width() // 2,
                    self.play_button.y + 10,
                ),
            )

        # Vẽ nút "Back"
        pygame.draw.rect(self.screen, (255, 0, 0), self.back_button)
        back_text = self.font.render("Back", True, (255, 255, 255))
        self.screen.blit(back_text, (self.back_button.x + 10, self.back_button.y + 10))

    def start(self):
        super().start()
        self.current_player = 1
        self.selected_character = None
        self.selected_characters = {}

    def exit(self):
        super().exit()