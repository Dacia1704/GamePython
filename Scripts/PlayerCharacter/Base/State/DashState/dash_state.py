import pygame
from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants

class DashState(CharacterState):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.start_time = 0
        self.current_sprite_index = 0

    # Base function
    def enter(self):
        super().enter()
        current_time = pygame.time.get_ticks()
        character = self.state_machine.character

        # Kiểm tra cooldown
        if current_time - character.last_dash_time < GameConstants.DASH_COOLDOWN:
            self.state_machine.change_state(self.state_machine.idle_state)
            return

        # Bắt đầu Dash
        self.start_time = current_time
        character.is_dashing = True
        character.vel_x = GameConstants.DASH_SPEED * (-1 if character.flip else 1)
        character.last_dash_time = current_time  # Lưu thời gian bắt đầu Dash

    def exit(self):
        super().exit()
        character = self.state_machine.character
        character.vel_x = 0
        character.is_dashing = False

    def update(self):
        super().update()
        current_time = pygame.time.get_ticks()
        character = self.state_machine.character

        # Kiểm tra trạng thái khác sau khi Dash kết thúc
        if current_time - self.start_time >= GameConstants.DASH_DURATION:
            character.vel_x = 0
            character.is_dashing = False
            self.state_machine.change_state(self.state_machine.idle_state)  # Chuyển sang trạng thái đứng yên
        else:
            # Di chuyển nhân vật
            character.rect.x += character.vel_x

            # Giới hạn không vượt màn hình
            if character.rect.left < 0 or character.rect.right > GameConstants.SCREEN_WIDTH:
                character.rect.x -= character.vel_x

        # Animation logic
        self.update_sprite_animation(
            character.dash_spritesheet[0], 
            character.dash_spritesheet[2], 
            False
        )

    # Animation
    def draw(self, surface):
        super().draw(surface)
        character = self.state_machine.character

        # Tính toán offset để hiển thị đúng vị trí
        offsetx = character.dash_spritesheet[3] * character.dash_spritesheet[1]
        if character.flip:
            offsetx = character.dash_spritesheet[4] * character.dash_spritesheet[1]
        offsety = character.dash_spritesheet[5] * character.dash_spritesheet[1]

        # Lấy frame hiện tại từ spritesheet và áp dụng hiệu ứng lật
        img = pygame.transform.flip(
            character.dash_spritesheet[0][self.current_sprite_index], 
            character.flip, 
            False
        )
        surface.blit(img, (character.rect.x - offsetx, character.rect.y - offsety))
