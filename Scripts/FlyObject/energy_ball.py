from Scripts.FlyObject.fly_object_base import FlyObjectBase

class EnergyBall(FlyObjectBase):
  def __init__(self,rect,direction,player,target,screen,sprite_sheet) :
    FlyObjectBase.__init__(self,rect,direction,player,target,screen,sprite_sheet)
