# Importing the Libraries and the modules
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

# Below are the method that are used to move the red parts, blue parts and green parts from the tray on to the kit 
 def _remove_part_from_bin(self, bin):
      current_quantity = current_state["bins"][f"bin{bin}"]['part_quantity']
      print(current_quantity)
      
 def _pickup_red_part(self, bin):
     _enable = True
     Gripper.activate_gripper(self)
     print(f"pickup_part({ self._name} , from bin { bin} ,red part  )")
     
 def _place_red_part(self, tray, agv):
     _enable = False
     Gripper.deactivate_gripper(self)
     print(f"place_part({ self._name} , place red part in { tray} tray that is on AGV {agv}")
     
 def _pickup_green_part(self, bin):
      _enable = True
      Gripper.activate_gripper(self)
      print(f"pickup_part({ self._name} , from bin { bin} ,green part  )")
      
 def _place_green_part(self, tray, agv):
      _enable = False
      Gripper.deactivate_gripper(self)
      print(f"place_part({ self._name} , place green part in { tray} tray that is on AGV {agv}")    
      

 def _pickup_blue_part(self, bin):
      _enable = True
      Gripper.activate_gripper(self)
      print(f"pickup_part({ self._name} , from bin { bin} ,blue part  )")
      
 def _place_blue_part(self, tray, agv):
      _enable = False
      Gripper.deactivate_gripper(self)
      print(f"place_part({ self._name} , place blue part in { tray} tray that is on AGV {agv}")       
      
