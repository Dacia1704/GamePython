from Scripts.PlayerCharacter.Base.State.SkillState.skill_state import SkillState
from Scripts.game_constants import GameConstants
from Scripts.Audio.audio_manager import AudioManager
import pygame
class RockLeeSkill2State(SkillState):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.isTeleport = False

    def enter(self):
        super().enter()
        AudioManager.get_instance().play_sfx(self.state_machine.character.skill_2_sfx_name)
        self.skill_collider_animations = GameConstants.ROCKLEE_SKILL2_COLLIDER_ANIMATIONS
        self.update_knock_back_force_target([5, 20], 150)
        self.isTeleport = False
    
    def exit(self):
        AudioManager.get_instance().stop_sfx(self.state_machine.character.skill_2_sfx_name)
        super().exit()

    def update(self):
        super().update()
        self.update_sprite_animation(self.state_machine.character.skill2_spritesheet[0],
                                     self.state_machine.character.skill2_spritesheet[2], False)

    def skill_attack_enter(self):
        super().skill_attack_enter()
        if not self.state_machine.character.is_using_skill:
            self.state_machine.character.target.dam_take = 20
            self.state_machine.character.mana_consume = 30
            # execute attack
            self.state_machine.character.is_using_skill = True
        self.state_machine.character.mana -= self.state_machine.character.mana_consume

    # animation
    def draw(self, surface):
        super().draw(surface)
        self.draw_skill_animation(surface, self.state_machine.character.skill2_spritesheet,
                                  GameConstants.ROCKLEE_SKILL2_COLLIDER_DICTIONARY)

    def draw_skill_animation(self, surface, sprite_sheet_data, animation_collider_dictionary):
        skill_sprite_sheet = sprite_sheet_data

        if self.current_sprite_index == len(skill_sprite_sheet[0]) - 1:
            if self.is_show_last_frame and self.is_last_frame_animation_cooldown_finished:
                self.state_machine.character.is_using_skill = False
                self.is_show_last_frame = False
            else:
                self.is_show_last_frame = True

        offsetx = skill_sprite_sheet[3] * skill_sprite_sheet[1]
        if self.state_machine.character.flip:
            offsetx = skill_sprite_sheet[4] * skill_sprite_sheet[1]
        offsety = skill_sprite_sheet[5] * skill_sprite_sheet[1]

        img = pygame.transform.flip(skill_sprite_sheet[0][self.current_sprite_index], self.state_machine.character.flip,
                                    False)
        surface.blit(img,
                     (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))

        if self.current_sprite_index in self.skill_collider_animations:
            collider_rect_props = animation_collider_dictionary.get(self.current_sprite_index)
            self.state_machine.character.draw_attack_area_collider(collider_rect_props[0], collider_rect_props[1],
                                                                   self.state_machine.character.target)

        if self.current_sprite_index == 5 and not self.isTeleport:
            self.state_machine.character.rect = pygame.Rect((self.state_machine.character.target.rect.x,
                                                             self.state_machine.character.target.rect.y,
                                                             self.state_machine.character.rect.width,
                                                             self.state_machine.character.rect.height))
            self.isTeleport = True
