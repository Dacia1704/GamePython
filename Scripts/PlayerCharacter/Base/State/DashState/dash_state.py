import pygame
from Scripts.PlayerCharacter.Base.State.character_state import CharacterState
from Scripts.Input.game_input import GameInput
from Scripts.game_constants import GameConstants

class DashState(CharacterState):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.dash_duration = 200  # Thời gian dash (ms)
        self.dash_speed = 15  # Tốc độ dash
        self.start_time = 0

    def enter(self):
        super().enter()
        self.start_time = pygame.time.get_ticks()
        self.state_machine.character.is_dashing = True
        # Vận tốc dash theo hướng
        self.state_machine.character.vel_x = self.dash_speed * (-1 if self.state_machine.character.flip else 1)

    def update(self):
        current_time = pygame.time.get_ticks()
        character = self.state_machine.character

        # Kết thúc Dash nếu hết thời gian
        if current_time - self.start_time >= self.dash_duration:
            character.vel_x = 0
            character.is_dashing = False
            self.state_machine.change_state(self.state_machine.idle_state)  # Trở lại trạng thái Idle
        else:
            # Cập nhật vị trí
            character.rect.x += character.vel_x

            # Giới hạn không vượt màn hình
            if character.rect.left < 0 or character.rect.right > GameConstants.SCREEN_WIDTH:
                character.rect.x -= character.vel_x

    
        
        # Kiểm tra các trạng thái khác chỉ sau khi Dash kết thúc
        if current_time - self.start_time >= self.dash_duration:
            self.on_idle()
            self.on_move()

    def exit(self):
        self.state_machine.character.vel_x = 0
        self.state_machine.character.is_dashing = False
    def draw_dash_effect(self, surface, character):
    # Số lượng frame animation muốn hiển thị
        num_frames = len(self.state_machine.character.dash_spritesheet)
        for i in range(num_frames):
            alpha = max(0, 255 - i * 50)  # Giảm độ trong suốt theo frame
            # Lấy từng frame từ dash_spritesheet
            trail_image = self.state_machine.character.dash_spritesheet[i].copy()  # Lấy frame thứ i
            trail_image.set_alpha(alpha)
            # Tính vị trí của hiệu ứng dash dựa trên frame
            offset = i * -10 * (-1 if character.flip else 1)  # Điều chỉnh khoảng cách dựa vào hướng của nhân vật
            surface.blit(trail_image, (character.rect.x + offset, character.rect.y))