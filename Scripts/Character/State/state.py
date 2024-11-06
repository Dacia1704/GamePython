from abc import ABC, abstractmethod

class State():
  #update state
  @abstractmethod
  def enter(self):
    pass
  @abstractmethod
  def exit(self):
    pass
  @abstractmethod
  def update(self):
    pass