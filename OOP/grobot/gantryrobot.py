import sys
sys.path.insert(1, "C:/Users/nisar/Desktop/Projects/rwa2_upadhyay_nisargkumar")    
from gripper.gripper import*
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

class GantryRobot(BaseRobot):
 """
 This is the class of the gantry robot

     Args:
     BaseRobot (class): This the parent class from which attributes and methods are inherited
 """
 def __init__(self):
  """
  This is the function where all the attributes used by the class are defined
  """
  super().__init__(name="Gantry", payload=15, weight=500, bins=['bin3', 'bin4'])
  self._small_rail_length = 12
  self._long_rail_length = 20
  self._small_rail_height = 5
  self._long_rail_height = 4.75
 
    
 def _pickup_tray(self, tray):

      """
      This is the method that is used to pick up the tray from the table
      """
      _enable = True
      Gripper.activate_gripper(self)
      print(f"pickup_tray({ self._name} , pick up {tray} tray from the table )")
      
      

     
 def _place_tray(self, tray, agv):

      
     """
      This is the method that is used to place the tray on the agv
     """
     _enable = False
     Gripper.deactivate_gripper(self)
     print(f"place_tray({ self._name} , { tray} tray  is placed on AGV { agv} )")
     

     