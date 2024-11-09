from abc import ABC, abstractmethod

class Attackable(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def draw_attack_area_collider(self,pos_relate_centerxy,size):
        pass