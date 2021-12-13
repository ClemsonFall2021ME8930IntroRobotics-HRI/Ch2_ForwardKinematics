# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:19:57 2021

@author: Ashley
"""
"""
Before Running the command it is expected that you read through the
command syntax from python API for CoppeliaSim. 
"""

# Make sure to have the server side running in CoppeliaSim: 
# in a child script of a CoppeliaSim scene, add following command
# to be executed just once, at simulation start:
#
# simRemoteApi.start(19999)
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

# then press play in Coppelia Sim, then run code to import sim and connect 
# Spyder to CoppeliaSim 


import math
import sim
import time 

print ('Program started')
sim.simxFinish(-1) # closes all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')
else:
        print ('Failed connecting to remote API server')
        print ('Program ended')

res,objs=sim.simxGetObjects(clientID,sim.sim_handle_all,sim.simx_opmode_blocking)
if res==sim.simx_return_ok:
        print ('Number of objects in the scene: ',len(objs))
else:
        print ('Remote API function call returned with error code: ',res)

time.sleep(2)

#Getting object handlle
opMode=sim.simx_opmode_blocking
errorCode,base=sim.simxGetObjectHandle(clientID,"Base",opMode)
errorCode,link1=sim.simxGetObjectHandle(clientID,"Link1",opMode)
errorCode,link2=sim.simxGetObjectHandle(clientID,"Link2",opMode)
errorCode,dummy=sim.simxGetObjectHandle(clientID,"Dummy",opMode)
errorCode,target=sim.simxGetObjectHandle(clientID,"Target",opMode)

errorCode,J1=sim.simxGetObjectHandle(clientID,"Revolute_joint1",opMode)
errorCode,J2=sim.simxGetObjectHandle(clientID,"Revolute_joint2",opMode)

#Getting tip start position
errorCode, tip_position= sim.simxGetObjectPosition(clientID,dummy,base,sim.simx_opmode_oneshot_wait)

"""
Note that the CoppeliaSim coordinate system isn't configured according to
the example problem. The following varibale chnages will take place due to this:
x in the illustration is x in CoppeliaSim
y in the illustration is z in CoppeliaSim
z in the illustration is y in CoppeliaSim.
The illustration assumes the robot is flat. In reality, the R joints create some distance in the illustrations z-direction.
This is ignored in teh code.

The actual calculation doesn't change just the naming of variable changes to resemble the coordinate system in Coppeliasim
"""

length_one = 1
length_two = 0.5
#the length of link 1 and link 2 respectively in meters

"""
Angles were made negative for the CoppeliaSim simulation due to axis orientation
However, the absolute was taken of all angles during the calculation of the joint positions to counteract this for the illustration set up
"""

alpha_deg = -60
#the angle between link 1 and the x-axis in degrees
alpha_rad = math.radians(alpha_deg)
#convert to radians

beta_deg = -30
#the angle between link 2 and the x-axis in degrees
beta_rad = math.radians(beta_deg)

# Setting the base position
x0 = 0
z0 = 0.5-0.05 #base length

"""
ALL lengths have a -0.05 to account for the joint not being centered at the end of the base link
"""

# Finding Joint 2 position
x1 = x0 + (length_one-0.10)*math.cos(abs(alpha_rad))
z1 = z0 + (length_one-0.10)*math.sin(abs(alpha_rad))

# Finding End Effector position
x2 = x1 + (length_two-0.05)*math.cos(abs(beta_rad))
z2 = z1 + (length_two-0.05)*math.sin(abs(beta_rad))

"""
For smoother simulation -> only 1% of the joint values every loop
"""
#joint 1
for i in range(1,100+1):
  J1a = i*0.01*alpha_rad;
  errorcode = sim.simxSetJointPosition(clientID,J1,J1a,sim.simx_opmode_oneshot_wait)
#joint 2  
for i in range(1,100+1):
  J2a = i*0.01*beta_rad;
  errorcode = sim.simxSetJointPosition(clientID,J2,J2a,sim.simx_opmode_oneshot_wait)

sim.simxFinish(clientID)

print("The end effectors calculated x-position is {}, and z-position is {}".format(round(x2,4), round(z2,4)))