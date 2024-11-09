from Scripts.PlayerCharacter.Base.State.NomalAttackState.nomal_attack_state import NomalAttackState
import pygame
class NarutoNomalAttack2State(NomalAttackState):
  def update(self):
    super().update()
    self.update_sprite_animation(self.state_machine.character.nomal_attack2_spritesheet[0],self.state_machine.character.nomal_attack2_spritesheet[2],False)

  def nomal_attack(self):
    super().nomal_attack()
    if not self.state_machine.character.is_nomal_attacking:
      #execute attack
      self.state_machine.character.is_nomal_attacking = True
      attacking_rect = pygame.Rect(self.state_machine.character.rect.centerx - (2 * self.state_machine.character.rect.width * self.state_machine.character.flip), self.state_machine.character.rect.y, 2 * self.state_machine.character.rect.width, self.state_machine.character.rect.height)
      pygame.draw.rect(self.state_machine.screen_surface, (0,255,0),attacking_rect)
      # if attacking_rect.colliderect(target.rect):
      #   target.health -= 10
      #   target.hit = True

  # animation
  def draw(self, surface):
    nomal_attack_sprite_sheet = self.state_machine.character.nomal_attack2_spritesheet

    if self.current_sprite_index == len(nomal_attack_sprite_sheet[0])-1:
      if self.is_show_last_frame:
        self.state_machine.character.is_nomal_attacking = False
        self.is_show_last_frame = False
      else:
        self.is_show_last_frame = True
    
    offsetx = nomal_attack_sprite_sheet[3] * nomal_attack_sprite_sheet[1]
    offsety = nomal_attack_sprite_sheet[4] * nomal_attack_sprite_sheet[1]
    img = pygame.transform.flip(nomal_attack_sprite_sheet[0][self.current_sprite_index], self.state_machine.character.flip, False)
    surface.blit(img, (self.state_machine.character.rect.x - offsetx, self.state_machine.character.rect.y - offsety))

