def start():
    """
    Function that will start the program and all the dictonaries that are used in the program is listed here
    """
    
    global robot
    global tray
    global bin1
    global bin2
    global bin3
    global bin4
    global agv
    global kitting_tray

    
    kitting_tray = {"location":{"on_table":True,
                                "on_agv": False}}
    robot = {"floor_robot":{"f_gripper" : False},
             "celing_robot":{"c_gripper" : False}}
    

    
    bin1 ={"r" : 0,
         "g" : 0,
         "b" : 0}
    bin2 = {"r" : 0,
         "g" : 0,
         "b" : 0}
    bin3 = {"r" : 0,
         "g" : 0,
         "b" : 0}
    bin4 = {"r" : 0,
         "g" : 0,
         "b" : 0}
    

    
def input_data():
    """
    This function will take and show all the data that is provided by the user.
    The data will cotains both initial and goal state
    This function will also update the dictonarirs according to the user input
    """
    
    
    global tray
    global agv
    global bin_r
    global r_p_t
    global bin_g
    global g_p_t
    global bin_b
    global b_p_t
    global assemble

    

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
                             if (tray == "y" or tray == "g"):
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
                                                  
                                                 
                                                   
    if bin_r ==1:
        bin1["r"] = r_p
    elif bin_r == 2:
        bin2["r"] = r_p
    elif bin_r ==3:
            bin3["r"] = r_p
    else:
        bin4["r"] = r_p
        
    if bin_g ==1:
            bin1["g"] = g_p
    elif bin_g == 2:
            bin2["g"] = g_p
    elif bin_g ==3:
                bin3["g"] = g_p
    else:
            bin4["g"] = g_p
            
    if bin_b ==1:
            bin1["b"] = b_p
    elif bin_b == 2:
            bin2["b"] = b_p
    elif bin_b ==3:
                bin3["b"] = b_p
    else:
            bin4["b"] = b_p
                                            
                     

def tray_movenment(tray_variable):
    """
    This function will move the tray from the table to the gripper

    Args:
        tray_variable (str): Color of the tray
    """
    if tray_variable == "g":
        if robot["celing_robot"]["c_gripper"] == False:
            if kitting_tray['location']["on_table"]==True:
                print("pickup_tray(robot_ceiling, gray_tray, gray_tray_table)")
                robot["celing_robot"]["c_gripper"] = True
                kitting_tray['location']["on_table"]=False
                
    if tray_variable == "y":
        if robot["celing_robot"]["c_gripper"] == False:
            if kitting_tray['location']["on_table"]==True:
               print("pickup_tray(robot_ceiling, yellow_tray, yellow_tray_table)") 
               robot["celing_robot"]["c_gripper"] = True
               kitting_tray['location']["on_table"]=False
  
               
def tray_movenment_agv(tray_variable,agv):
    """
    This function will move the tray from the gripper and will place it on top of the agv

    Args:
        tray_variable (str): The color of the tray
        agv (str): Number of the agv on which the tray has to be placed
    """
    if tray_variable == "g":
     if robot["celing_robot"]["c_gripper"] == True:
        if kitting_tray['location']["on_table"]==False:
            print(f"place_tray(robot_ceiling, gray_tray,agv{agv})")
            robot["celing_robot"]["c_gripper"] = False
            kitting_tray['location']["on_table"]=False
            kitting_tray['location']["on_agv"]=True
    if tray_variable == "y":        
     if robot["celing_robot"]["c_gripper"] == True:
         if kitting_tray['location']["on_table"]==False:
                print(f"place_tray(robot_ceiling, yellow_tray,agv{agv})")
                robot["celing_robot"]["c_gripper"] = False
                kitting_tray['location']["on_table"]=False
                kitting_tray['location']["on_agv"]=True
            
def red_parts_movenment(bin_r,r_p_t,tray,agv):
    """
    This function will move the red parts according to the user from the bin and will place it on the AGV

    Args:
        bin_r (str): The value of the bin in which red parts are located
        r_p_t (str): Red parts that will be delivered to the assemble station
        tray (str): Color of the tray
        agv (str): The agv that will be used to deliver the parts to the station
    """
    
    if int(bin_r) == 1 or int(bin_r) == 2:
        
        if robot["floor_robot"]["f_gripper"] == False:
            if r_p_t != 0:
                x= int(r_p_t)
                while x!=0:
                
                    print(f"pick_red_part(floor_robot, bin{bin_r},red_part)")
                    robot["floor_robot"]["f_gripper"] = True
                    if robot["floor_robot"]["f_gripper"] == True:
                        print(f"place_red_part(floor_robot, {tray}_tray,red_part,agv{agv})")
                        robot["floor_robot"]["f_gripper"] = False
                        x = x-1
      

     
                    
    if int(bin_r) == 3 or int(bin_r) == 4:
        
        if robot["celing_robot"]["c_gripper"] == False:
            if r_p_t != 0:
                x= int(r_p_t)
                while x!=0:
                
                    print(f"pick_red_part(celing_robot, bin{bin_r},red_part)")
                    robot["celing_robot"]["c_gripper"] = True
                    if robot["celing_robot"]["c_gripper"] == True:
                        print(f"place_red_part(celing_robot, {tray}_tray,red_part,agv{agv})")
                        robot["celing_robot"]["c_gripper"] = False
                        x = x-1
                        
        
def green_parts_movenment(bin_g,g_p_t,tray,agv):
    """
    This function will move the green parts according to the user from the bin and will place it on the AGV

    Args:
        bin_r (str): The value of the bin in which green parts are located
        r_p_t (str): Green parts that will be delivered to the assemble station
        tray (str): Color of the tray
        agv (str): The agv that will be used to deliver the parts to the station
    """   
    if int(bin_g) == 1 or int(bin_g) == 2:
        
        if robot["floor_robot"]["f_gripper"] == False:
            if g_p_t != 0:
                x= int(g_p_t)
                while x!=0:
                
                    print(f"pick_green_part(floor_robot, bin{bin_g},green_part)")
                    robot["floor_robot"]["f_gripper"] = True
                    if robot["floor_robot"]["f_gripper"] == True:
                        print(f"place_green_part(floor_robot, {tray}_tray,green_part,agv{agv})")
                        robot["floor_robot"]["f_gripper"] = False
                        x = x-1
      

     
                    
    
    if int(bin_g) == 3 or int(bin_g) == 4:
        
        if robot["celing_robot"]["c_gripper"] == False:
            if g_p_t != 0:
                x= int(g_p_t)
                while x!=0:
                
                    print(f"pick_green_part(celing_robot, bin{bin_g},green_part)")
                    robot["celing_robot"]["c_gripper"] = True
                    if robot["celing_robot"]["c_gripper"] == True:
                        print(f"place_green_part(celing_robot, {tray}_tray,green_part,agv{agv})")
                        robot["celing_robot"]["c_gripper"] = False
                        x = x-1

 
    
    
def blue_parts_movenment(bin_b,b_p_t,tray,agv):

    """
    This function will move the blue parts according to the user from the bin and will place it on the AGV

    Args:
        bin_r (str): The value of the bin in which blue parts are located
        r_p_t (str): Blue parts that will be delivered to the assemble station
        tray (str): Color of the tray
        agv (str): The agv that will be used to deliver the parts to the station
    """   
    if int(bin_b) == 1 or int(bin_b) == 2:
        
        if robot["floor_robot"]["f_gripper"] == False:
            if b_p_t != 0:
                x= int(b_p_t)
                while x!=0:
                
                    print(f"pick_blue_part(floor_robot, bin{bin_b},blue_part)")
                    robot["floor_robot"]["f_gripper"] = True
                    if robot["floor_robot"]["f_gripper"] == True:
                        print(f"place_blue_part(floor_robot, {tray}_tray,blue_part,agv{agv})")
                        robot["floor_robot"]["f_gripper"] = False
                        x = x-1        
                
    
    if int(bin_b) == 3 or int(bin_b) == 4:
        
        if robot["celing_robot"]["c_gripper"] == False:
            if b_p_t != 0:
                x= int(b_p_t)
                while x!=0:
                
                    print(f"pick_blue_part(celing_robot, bin{bin_b},blue_part)")
                    robot["celing_robot"]["c_gripper"] = True
                    if robot["celing_robot"]["c_gripper"] == True:
                        print(f"place_blue_part(celing_robot, {tray}_tray,blue_part,agv{agv})")
                        robot["celing_robot"]["c_gripper"] = False
                        x = x-1    
    
 
def agv_movenment(agv,assemble,tray):
    """
    This function will move the agv to the asemble station with the trays and the parts

    Args:
        agv (str): The agv that will deliver the parts
        assemble (str): The assemble station that is provided by the user
        tray (str): Color of the tray that will be delivered by the agv to the assemble station with the parts on it
    """
    if int(agv) == 1 or int(agv) == 2:
        if (int(assemble) == 1) or (int(assemble) ==2):
            print(f"ship_agv(agv{agv} , {tray}_tray , assemble{assemble})")
    
    if int(agv) == 3 or int(agv) == 4:
        if (int(assemble) == 3) or (int(assemble) ==4):
            print(f"ship_agv(agv{agv} , {tray}_tray , assemble{assemble})")     
    
                                       

 
if __name__ == "__main__": 
 start()
 input_data()



 tray_movenment(tray)
 tray_movenment_agv(tray,agv)

 red_parts_movenment(bin_r,r_p_t,tray,agv) 
 green_parts_movenment(bin_g,g_p_t,tray,agv)
 blue_parts_movenment(bin_b,b_p_t,tray,agv)  
                          
 agv_movenment(agv,assemble,tray)                             
 print("="*50)
                      

                    
                         
                  
                         
