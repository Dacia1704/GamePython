from Scripts.PlayerCharacter.Base.State.SkillState.skill_state import SkillState
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
import pygame


class SasukeSkill2State(SkillState):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.isTeleport = False

    def enter(self):
        super().enter()
        self.skill_collider_animations = GameConstants.SASUKE_SKILL2_COLLIDER_ANIMATIONS
        AudioManager.get_instance().play_sfx(self.state_machine.character.skill_2_sfx_name)
        self.update_knock_back_force_target([5, 0], 100)
        self.update_target_dam_take(GameConstants.SASUKE_SKILL_2_PROPS[0])
        self.isTeleport = False
        self.state_machine.character.mana -= self.state_machine.character.mana_consume_skill_2
    def exit(self):
        AudioManager.get_instance().stop_sfx(self.state_machine.character.skill_2_sfx_name)
        super().exit()
    def update(self):
        super().update()
        self.update_sprite_animation(self.state_machine.character.skill2_spritesheet[0],
                                     self.state_machine.character.skill2_spritesheet[2], False)

    def skill_attack(self):
        super().skill_attack()
        if not self.state_machine.character.is_using_skill:
            # execute attack
            self.state_machine.character.is_using_skill = True
       

    # animation
    def draw(self, surface):
        super().draw(surface)
        self.draw_skill_animation(surface, self.state_machine.character.skill2_spritesheet,
                                  GameConstants.SASUKE_SKILL2_COLLIDER_DICTIONARY)

    def draw_skill_animation(self, surface, sprite_sheet_data, animation_collider_dictionary):
        skill_sprite_sheet = sprite_sheet_data

        # Kiểm tra nếu là frame cuối cùng của hoạt ảnh
        if self.current_sprite_index == len(skill_sprite_sheet[0]) - 1:
            if self.is_show_last_frame and self.is_last_frame_animation_cooldown_finished:
                self.state_machine.character.is_using_skill = False
                self.is_show_last_frame = False
            else:
                self.is_show_last_frame = True

        # Tính toán offset để hiển thị sprite
        offsetx = skill_sprite_sheet[3] * skill_sprite_sheet[1]
        if self.state_machine.character.flip:
            offsetx = skill_sprite_sheet[4] * skill_sprite_sheet[1]
        offsety = skill_sprite_sheet[5] * skill_sprite_sheet[1]

        # Hiển thị sprite skill
        img = pygame.transform.flip(skill_sprite_sheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
        surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))

        # Xử lý vùng va chạm (collider) cho skill
        if self.current_sprite_index in self.skill_collider_animations:
            collider_rect_props = animation_collider_dictionary.get(self.current_sprite_index)
            self.state_machine.character.draw_attack_area_collider(collider_rect_props[0], collider_rect_props[1],
                                                                self.state_machine.character.target)

        # Thực hiện teleport nếu ở frame đúng và chưa teleport
        if self.current_sprite_index == 1 and not self.isTeleport:
            target_rect = self.state_machine.character.target.rect
            character_rect = self.state_machine.character.rect
            teleport_offset = 50  # Khoảng cách cố định giữa Sasuke và mục tiêu

            # Xác định hướng teleport dựa trên vị trí hiện tại của Sasuke
            if character_rect.centerx < target_rect.centerx:
                # Sasuke ở bên trái mục tiêu
                new_x = target_rect.left - character_rect.width - teleport_offset
                self.state_machine.character.flip = False  # Sasuke quay mặt sang phải
            else:
                # Sasuke ở bên phải mục tiêu
                new_x = target_rect.right + teleport_offset
                self.state_machine.character.flip = True  # Sasuke quay mặt sang trái

            # Giữ y cố định ở mặt đất, trừ chiều cao nhân vật để Sasuke không bị lệch lên
            new_y = GameConstants.GROUND_Y + character_rect.height  # Dùng GROUND_Y và trừ chiều cao của nhân vật

            # Cập nhật vị trí Sasuke (x, y)
            self.state_machine.character.rect = pygame.Rect(
                (new_x, new_y, character_rect.width, character_rect.height)
            )
            self.isTeleport = True
