# Importing the Libraries and the modules
import sys
sys.path.insert(1, "C:/Users/nisar/Desktop/Projects/rwa2_upadhyay_nisargkumar") 
class Gripper:
 """
 This the Gripper class which is attached to the linear as well as gantry robot
 """
 def __init__(self, name, weight=2, closing_speed=150):
  """
  This the function in which all the attributes that are used by the gripper class are defined

   Args:
       name (str): name of the robot
       weight (int): weight of the gripper. Defaults to 2.
       closing_speed (int): The speed of the gripper . Defaults to 150.
  """

  self._name = name
  self._weight = weight
  self._closing_speed = closing_speed
  self._enable = True
  self._object_held = None
  
# This code will encapsulate the class using @property method
 @property
 def name(self):
  return self._name

 @property
 def weight(self):
   return self._weight

 @property
 def closing_speed(self):
   return self._closing_speed

 @property
 def obeject_held(self):
  return self._object_held

 @obeject_held.setter
 def object_held(self):
  self._object_held = None
  
 def __str__(self):
  """
  This method will give the name of the robot

   Returns:
       str: name of the robot
  """

  return f"The gripper is attached to {self._name}"
 
 def activate_gripper(self):
  """
  This method will open the gripper to hold things
  """
  _enable = True
  if _enable == True:
    print("activate gripper")
     
 def deactivate_gripper(self):
  """
  This method will close the gripper to release things
  """
  _enable = False
  if _enable == False:
    print("deactivate gripper")
     
  
     

