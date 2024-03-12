# Importing the Libraries and the modules
from pprint import pprint
import sys
sys.path.insert(1, "C:/Users/nisar/Desktop/Projects/rwa2_upadhyay_nisargkumar") 
from utils.utils import*
from grobot.gantryrobot import*
from gripper.gripper import*
from robot.baserobot import BaseRobot

# This is the main Function 
def start():

 """
 This is the main function
 First the function will take the input from the user
 Second it will update the Dictonary which is imported from utlis according the user input and will display it
 Third it will call the necessary methods that are requried for the kitting from different modules
 Lastly it will print the plan for the kitting process based on user input
 """


# User will provide the input
 print("Bin that has red parts? [1,2,3,4]")         
 bin_r= input()
 if ((int(bin_r)==1) or (int(bin_r)==2) or (int(bin_r)==3) or (int(bin_r)==4)):
   
    print("How many red parts in the bin ? [0,4,9]")        
    r_p= input()
    
    if (int(r_p)== 4) or (int(r_p)== 9) or int(r_p)==0:
        print("Bin that has green parts? [1,2,3,4]")
        bin_g= input()
        if ((int(bin_g)==1) or (int(bin_g)==2) or (int(bin_g)==3) or (int(bin_g)==4)):
         if (bin_g != bin_r):
            print("How many green parts in the bin ? [0,4,9]")
            g_p= input()
            
            if (int(g_p)== 4) or (int(g_p)== 9 or int(g_p)==0):
             print("Bin that has blue parts? [1,2,3,4]")
             bin_b= input()
             if ((int(bin_b)==1) or (int(bin_b)==2) or (int(bin_b)==3) or (int(bin_b)==4)):
              if (bin_b != bin_r or bin_b != bin_g ):
                 print("How many blue parts in the bin [0,4,9]?") 
                 b_p= input()
                 if int(b_p)== 4 or int(b_p)== 9 or int(b_p)==0:
                     
                     print("AGV to use for kitting [1,2,3,4]")
                     agv = input()
                     if ((int(agv)==1) or (int(agv)==2) or (int(agv)==3) or (int(agv)==4)):
                         print("Select the tray [y]yellow, [g]ray")
                         tray = input()
                         if (tray == str("y") or tray == str("g")):
                             print("The number of red_part to put in the tray [0,1,2]")
                             r_p_t = input()
                             if (int(r_p_t)== 1) or (int(r_p_t)== 2) or (int(r_p_t)== 0):
                                 if int(r_p_t)<=int(r_p):
                                  print("The number of green_part to put in the tray [0,1,2]")
                                  g_p_t = input()
                                  if (int(g_p_t)== 1) or (int(g_p_t)== 2) or (int(g_p_t)== 0):
                                      if int(g_p_t)<=int(g_p):
                                       print("The number of blue_part to put in the tray [0,1,2]")
                                       b_p_t = input()
                                       if (int(b_p_t)== 1) or (int(b_p_t)== 2) or (int(b_p_t)== 0):
                                           if int(g_p_t)<=int(g_p):
                                            print("assembly station [1,2,3,4]")
                                            assemble = input()
                                            if (int(assemble) == 1) or (int(assemble) ==2):
                                             if (int(agv) == 1) or (int(agv) ==2):
                                                 print("solution is possible")
                                                 print("="*50)
                                                 if (int(assemble) == 3) or (int(assemble) ==4):
                                                  if (int(agv) == 3) or (int(agv) ==4):
                                                      print("solution is possible")
                                                      print("="*50)


# Update the current dictonary according to the user input

    
 if int(agv) == 1:
     if int(assemble)==1:
         
      del current_state["agvs"]

      u = {"agvs": { "possible_destination": assemble,
                 "AGV":agv }}
      current_state.update(u)
      
 if int(agv) == 1:
     if int(assemble)==2:
         
      del current_state["agvs"]

      u = {"agvs": { "possible_destination": assemble,
                 "AGV":agv }}
      current_state.update(u)
           
                        
 if int(agv) == 2:
     if int(assemble)==1:
         
      del current_state["agvs"]

      u = {"agvs": { "possible_destination":assemble,
                 "AGV":agv }}
      current_state.update(u)
      
 if int(agv) == 2:
     if int(assemble)==2:
         
      del current_state["agvs"]

      u = {"agvs": { "possible_destination": assemble,
                 "AGV":agv }}
      current_state.update(u)   

         

 if int(agv) == 3:
     if int(assemble)==3:
         
      del current_state["agvs"]

      u = {"agvs": { "possible_destination": assemble,
                 "AGV":agv }}
      current_state.update(u)
      
 if int(agv) == 3:
     if int(assemble)==4:
         
      del current_state["agvs"]

      u = {"agvs": { "possible_destination":assemble,
                 "AGV":agv }}
      current_state.update(u)
           
                        
 if int(agv) == 4:
     if int(assemble)==3:
         
      del current_state["agvs"]

      u = {"agvs": { "possible_destination": assemble,
                 "AGV":agv }}
      current_state.update(u)
      
 if int(agv) == 4:
     if int(assemble)==4:
         
      del current_state["agvs"]

      u = {"agvs": { "possible_destination": assemble,
                 "AGV":agv }}
      current_state.update(u) 
      
    
 if tray == str("y"):
     del current_state["trays"]
     u = {"trays":{'yellow_tray': {'location': 'table',
                                   'expected_parts':(int(r_p_t)+ int(b_p_t)+ int(g_p_t)), 
                                   'current_parts': 0 }}}
     current_state.update(u)
                 
 if tray == str("g"):
      del current_state["trays"]
      u = {"trays":{'gray_tray': {'location': 'table',
                                    'expected_parts':(int(r_p_t)+ int(b_p_t)+ int(g_p_t)), 
                                    'current_parts': 0 }}}
      current_state.update(u)              
                
 if int(bin_r) == 1:
     del current_state["bins"]["bin1"]
     u = {"bins":{"bin1":{'part_type': "Red Part",
                 'part_quantity': int(r_p)}},
          'bin2': {
              'part_type': None,
              'part_quantity': 0
          },
          'bin3': {
              'part_type': None,
              'part_quantity': 0
          },
          'bin4': {
              'part_type': None,
              'part_quantity': 0
          },}
          
     current_state.update(u)
     
 if int(bin_r) == 3:
      del current_state["bins"]["bin3"]
      u = {"bins":{"bin3":{'part_type': "Red Part",
                  'part_quantity': int(r_p)}},
           'bin2': {
               'part_type': None,
               'part_quantity': 0
           },
           'bin1': {
               'part_type': None,
               'part_quantity': 0
           },
           'bin4': {
               'part_type': None,
               'part_quantity': 0
           },}
      current_state.update(u)
     
 if int(bin_r) == 4:
      del current_state["bins"]["bin4"]
      u = {"bins":{"bin4":{'part_type': "Red Part",
                  'part_quantity': int(r_p)}},
           'bin2': {
               'part_type': None,
               'part_quantity': 0
           },
           'bin3': {
               'part_type': None,
               'part_quantity': 0
           },
           'bin1': {
               'part_type': None,
               'part_quantity': 0
           },}
      current_state.update(u)
      
 if int(bin_r) == 2:
      del current_state["bins"]["bin2"]
      u = {"bins":{"bin2":{'part_type': "Red Part",
                  'part_quantity': int(r_p)}},
           'bin1': {
               'part_type': None,
               'part_quantity': 0
           },
           'bin3': {
               'part_type': None,
               'part_quantity': 0
           },
           'bin4': {
               'part_type': None,
               'part_quantity': 0
           },} 
      current_state.update(u)

 if int(bin_b) == 1:
     del current_state["bin1"]
     u = {"bin1":{'part_type': "blue Part",
                 'part_quantity': int(b_p)}}
     current_state["bins"].update(u)
     
 if int(bin_b) == 3:
      del current_state["bin3"]
      u = {"bin3":{'part_type': "blue Part",
                  'part_quantity': int(b_p)}}
      current_state["bins"].update(u)
     
 if int(bin_b) == 4:
      del current_state["bin4"]
      u = {"bin4":{'part_type': "blue Part",
                  'part_quantity': int(b_p)}}
      current_state["bins"].update(u)
 if int(bin_b) == 2:
      del current_state["bin2"]
      u = {"bin2":{'part_type': "blue Part",
                  'part_quantity': int(b_p)}}
      current_state["bins"].update(u)
      
 if int(bin_g) == 1:
     del current_state["bin1"]
     u = {"bin1":{'part_type': "green Part",
                 'part_quantity': int(g_p)}}
     current_state["bins"].update(u)
     
 if int(bin_g) == 3:
      del current_state["bin3"]
      u = {"bin3":{'part_type': "green Part",
                  'part_quantity': int(g_p)}}
      current_state["bins"].update(u)
     
 if int(bin_g) == 4:
      del current_state["bin4"]
      u = {"bin4":{'part_type': "green Part",
                  'part_quantity': int(g_p)}}
      current_state["bins"].update(u)
 if int(bin_g) == 2:
      del current_state["bin2"]
      u = {"bin2":{'part_type': "green Part",
                  'part_quantity': int(g_p)}}
      current_state["bins"].update(u)
   


 del current_state["kit"]
 u = {"kit":{'agv': int(agv), 'complete': False, 'tray': tray}}
 current_state.update(u)
 
 s = (list(current_state.keys()))
 del current_state[s[4]]
 print("*" * 50)
 print("Updated Dictonaty") # Display the updated dictonary
 pprint(current_state)
       
 print("*" * 50)
 
 gantryrobot= BaseRobot(name = "gantry", payload=15, weight=500) # Object for the gantry robot from the baserobot class
 linearrobot = BaseRobot(name="UR10", payload=10, weight=200) # Object for the linear robot from the baserobot class
 gp = GantryRobot() # Object from the Gantryrobot class

# Placing the try from the table on the agv
 gp._pickup_tray(tray)
 gp._place_tray(tray, agv)
 
# Movenment of the red parts
 if int(bin_r) == 3 or int(bin_r) == 4:
     if r_p_t != 0:
         x= int(r_p_t)
         while x!=0:
          gantryrobot._pickup_red_part(bin_r)
          gantryrobot._place_red_part(tray,agv)
          x = x-1
          
 if int(bin_r) == 2 or int(bin_r) == 1:
     if r_p_t != 0:
         x= int(r_p_t)
         while x!=0:
          linearrobot._pickup_red_part(bin_r)
          linearrobot._place_red_part(tray,agv)
          x = x-1

# Movenment of the green parts    
 if int(bin_g) == 3 or int(bin_g) == 4:
     if g_p_t != 0:
         x= int(g_p_t)
         while x!=0:
          gantryrobot._pickup_green_part(bin_g)
          gantryrobot._place_green_part(tray,agv)
          x = x-1
          
 if int(bin_g) == 2 or int(bin_g) == 1:
     if g_p_t != 0:
         x= int(g_p_t)
         while x!=0:
          linearrobot._pickup_green_part(bin_g)
          linearrobot._place_green_part(tray,agv)
          x = x-1 

# Movenment of the blue parts
 if int(bin_b) == 3 or int(bin_b) == 4:
     if b_p_t != 0:
         x= int(b_p_t)
         while x!=0:
          gantryrobot._pickup_blue_part(bin_b)
          gantryrobot._place_blue_part(tray,agv)
          x = x-1
          
 if int(bin_b) == 2 or int(bin_b) == 1:
     if b_p_t != 0:
         x= int(b_p_t)
         while x!=0:
          linearrobot._pickup_blue_part(bin_b)
          linearrobot._place_blue_part(tray,agv)
          x = x-1 
 
 
 print("The kit is complete")

# Shipping the agv to the assemble station         
 if int(agv) == 1 or int(agv) == 2:
        if (int(assemble) == 1) or (int(assemble) ==2):
            print(f"ship_agv(agv{agv} , {tray}_tray , assemble{assemble})")
    
 if int(agv) == 3 or int(agv) == 4:
        if (int(assemble) == 3) or (int(assemble) ==4):
            print(f"ship_agv(agv {agv} , {tray}_tray , assemble {assemble})")  

 # Main program            
if __name__ == '__main__':
    start() # Calling the main function


    