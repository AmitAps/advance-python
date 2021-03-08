class Person:
  def __init__(self):
    self.name = 'Amit'
    self.__lastname = 'Singh'

  def PrintName(self):
    return self.name +' ' + self.__lastname
