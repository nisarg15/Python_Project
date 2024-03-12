import sys
sys.path.insert(1, "C:/Users/nisar/Desktop/Projects/rwa2_upadhyay_nisargkumar")    
from gripper.gripper import*
from robot.baserobot import *
from main.main import*

class BaseRobot():
 """
 This class is the base robot class which is the parent class of the linear and gantry robot
 """
 def __init__(self, name, payload, weight, bins=[], category="industrial"):
  """
  This the function in which all the attributes that are used by the baserobot class are defined

      Args:
          name (int): name of the robot
          payload (int): load the robot can carry
          weight (int): weight of the robot
  """
  self._name = name
  self._category = category
  self._payload = payload
  self._weight = weight
  self._gripper: Gripper = None
  self._accessible_bins = bins

# This code will encapsulate the class using @property method
 @property
 def name(self):
  return self._name

 @property
 def category(self):
  return self._category

 @property
 def payload(self):
  return self._payload

 @property
 def weight(self):
  return self._weight

 @property
 def bins(self):
  return self._accessible_bins

 @property
 def gripper(self):
  return self.Gripper

 @gripper.setter

 def gripper(self):
  self.Gripper = None 

  
class LinearRobot(BaseRobot):

 def __init__(self):
  """ 
  This the method where all the attributes of the class are stored
  """
  super().__init__(name="UR10", payload=10, weight=200, bins=['bin1', 'bin2'])
  self._linear_rail_length = 10
