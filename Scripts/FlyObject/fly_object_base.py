from Scripts.Attackable.attackable import Attackable
import pygame
from Scripts.game_constants import GameConstants
class FlyObjectBase(Attackable):
  def __init__(self,rect,direction,player,target,screen,sprite_sheet) :
    Attackable.__init__(self)
    self.rect = pygame.Rect((rect[0],rect[1],rect[2],rect[3]))
    self.direction = direction
    self.target = target
    self.player = player
    self.is_hitting = False
    self.screen = screen
    self.sprite_sheet = sprite_sheet
    self.current_sprite_index = 0
    self.update_animation_time = pygame.time.get_ticks()
    self.is_out_screen = False

  def update(self):
    self.move()
    self.draw(self.screen)
    self.draw_attack_area_collider([-self.rect.width/2,-self.rect.height/2],[self.rect.width,self.rect.height],self.target)
    self.update_sprite_animation(self.sprite_sheet[0],self.sprite_sheet[2],True)

  def move(self):
    self.rect.x += self.direction[0]
    self.rect.y += self.direction[1]

    if self.rect.left > GameConstants.SCREEN_WIDTH or self.rect.right < 0 or self.rect.bottom > GameConstants.SCREEN_HEIGHT or self.rect.top < 0:
      self.is_out_screen = True
  
  def draw(self,screen):
    pygame.draw.rect(screen,(255,0,0),self.rect)
    offsetx = self.sprite_sheet[3] * self.sprite_sheet[1] 
    if self.direction[0]<0:
      offsetx = self.sprite_sheet[4] * self.sprite_sheet[1]
    offsety = self.sprite_sheet[5] * self.sprite_sheet[1]
    img = pygame.transform.flip(self.sprite_sheet[0][self.current_sprite_index], self.direction[0] < 0, False)
    screen.blit(img, (self.rect.x - offsetx, self.rect.y - offsety))

  def draw_attack_area_collider(self, pos_relate_centerxy, size,target):
    attacking_rect = None
    if self.direction[0]>0:
      attacking_rect = pygame.Rect(self.rect.centerx + pos_relate_centerxy[0], self.rect.centery + pos_relate_centerxy[1],size[0] , size[1])
    else:
      attacking_rect = pygame.Rect(self.rect.centerx - pos_relate_centerxy[0] - size[0], self.rect.centery + pos_relate_centerxy[1], size[0], size[1])
    #pygame.draw.rect(self.screen, (0,255,0),attacking_rect)
    if attacking_rect.colliderect(target.damable_rect):
      self.is_hitting = True
      target.is_hitting = True
  
  def update_sprite_animation(self,sprite_sheet,animation_cooldown,loop):
    max = len(sprite_sheet)
    if pygame.time.get_ticks() - self.update_animation_time > animation_cooldown: 
      self.current_sprite_index +=1
      self.update_animation_time = pygame.time.get_ticks()
    if self.current_sprite_index >= max:
      if loop:
        self.current_sprite_index = 0
      else:
        self.current_sprite_index = max-1
