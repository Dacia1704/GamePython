from abc import ABC, abstractmethod

class Damable(ABC):
    def __init__(self):
        self.dam_take = 0
        self.damable_rect = None
    def reset_damable(self):
        self.dam_take = 0
    @abstractmethod
    def draw_get_dam_area_collider(self,pos_relate_centerxy,size):
        pass