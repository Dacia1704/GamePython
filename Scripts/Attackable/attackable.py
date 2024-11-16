from abc import ABC, abstractmethod

class Attackable(ABC):
    def __init__(self):
        self.damage = 0
        self.attackable_rect = None

    def reset_attackable(self):
        self.damage = 0
        self.attackable_rect = None

    @abstractmethod
    def draw_attack_area_collider(self,pos_relate_centerxy,size):
        pass