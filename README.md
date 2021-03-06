# Ch2_ForwardKinematics

## Problem Statement

Finding the forward kinematic solution of a 2-link planar manipulator. Use the found soluton to wriate a phyton code and simulate in CoppeliaSim.

## Pre-requisites:

- Software: CoppeliaSim (for simulation), Spyder (for Python coding)
- Basic Python syntax
- Understanding of the python remote API commands for CoppeliaSim

## Solution

<img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20-%20Simulation%20-%20DH%20Examples-09.png" width="400">

Assume the link lengths to be l<sub>1</sub< and l<sub>2</sub>, respectivley, with coresponding joint angles of &alpha; and &beta;.

To find the manipulator's forward knematic, we need to find the end effectors position: x<sub>2</sub>, y<sub>2</sub>.

First, we should find the positioning of the second joint located at the end of link 1:

x<sub>1</sub> = l<sub>1</sub>\*cos(&alpha;)

y<sub>1</sub> = l<sub>1</sub>\*sin(&alpha;)

These are then used to find the end effectors position: x<sub>2</sub>, y<sub>2</sub>; at the end of link 2.

x<sub>2</sub> = x<sub>1</sub> + l<sub>2</sub>\*cos(&alpha;+&beta;)

y<sub>2</sub> = y<sub>1</sub> + l<sub>2</sub>\*sin(&alpha;+&beta;)

## Simulation

### Scene setup:
  
Open the "TwoPlanarManipulator_Simulation.ttt" file. For this problem, we create the manipulate with two main add actions: "Add > Primitive Shape >  Cuboid" for the linkages and "Add > Joint > Revolute" for the joints. As each link and joint is added, rename them by double clicking on the name field in the Scene Hierachy, so they represent the correct order: Link1, Link2, Revolute_joint1, Revolute_joint2, etc.
  
| Add Link | Add Joint |
| :------: | :-------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20b%20-%20Simulation%20-%20AddCuboid.PNG" width="400"> | <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20c%20-%20Simulation%20-%20AddRevolute.PNG" width="400"> |

To start, the base needs to be created by set the dimensions of the first cuboid added to 0.1 for the x and y components and 0.5 for the z component.
  
| Setting the Base Dimensions |
| :-------------------------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20d%20-%20Simulation%20-%20SettingLinkLength0.5.PNG" width="400"> |
       
This is repeated for links 1 and 2 with lengths of 1 and 0.5, respectively.
       
Once a joint is added, to change the length to 0.3m and diameter to 0.1m, double click on the blue icon in the Scene hierachy to bring up the Scene Object Properties dialogue box.
       
| Setting the Joint Dimensions |
| :--------------------------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20e%20-%20Simulation%20-%20SettingJointDimensions.PNG" width="400"> |
  
To move each of these objects/items to their respective locations, click on the object/item to be moved and click on "Object/Item Translation/Position". When the "Mouse Translation" tab is selected, the object/item can be dragged around the screen in the direction(s) that are selected. When the "Translation" tab is selected, type in the distance to move the object/item in the specified direction then click on the respective "translate sel." button for the object to be moved.
  
| Mouse Translation | Translation |
| :---------------: | :---------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20f%20-%20Simulation%20-%20MouseTranslation.PNG" width="400"> | <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20g%20-%20Simulation%20-%20Translation.PNG" width="400"> |
  
To rotate each of these objects/items to their resepctive orientations (if needed), click on the object/item to be rotated and click on "Object/Item Rotation/Orientation". When the "Mouse Rotation" tab is selected, the object/item can be dragged about the axis selected. When the "Rotation" tab is selected, type in the rotation amount to move the object/item about the specificed axis then click on the respective "rotate sel." button for the object to be rotated.
  
| Mouse Rotation | Rotation |
| :---------------: | :---------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20h%20-%20Simulation%20-%20MouseRotation.PNG" width="400"> | <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20i%20-%20Simulation%20-%20Rotation.PNG" width="300"> |
  
Next, it must be defined on where the manipulator currently is. To do this, "Add > Dummy". Add a Dummy and center it at the end of the final link (link 2).
  
It is important to make sure all the correct properties are set. For each link, double click on the cuboid logo to bring up the "Scene Object Properties". For all cuboids, stay in the "Shape" tab, click on "Show Dynamic Properties Dialog" and unselect "Body is dynamic". If this is not deselected, then the link will fall to the ground due to gravity. For the base cuboid, click on the "Common" tab and select "Object is model base". For each joint, double click on the revolute joint logo to bring up the "Scene Object Properties". For all joints, stay in the "Joint" tab and change the Mode to "Passive Mode" to enable to the joint to drive the connected link.
  
| All Cuboids Properties | Base Cuboid Properties | R Joint Properties |
| :--------------------: | :--------------------: | :----------------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20j%20-%20Simulation%20-%20AllCuboidProperties.PNG" width="400"> | <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20k%20-%20Simulation%20-%20BaseCuboidProperties.PNG" width="300"> | <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20l%20-%20Simulation%20-%20BaseCuboidProperties.PNG" width="300"> |
  
The last change to the objects to make is to assign the correct hierarchy. To do so, drag the child object on top of the parent object to make the hierarchy link. It should look like this:
  
| Hierarchy |
| :-------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20n%20-%20Simulation%20-%20Hierarchy.PNG" width="400"> |
  
Finally, the connection for CoppeliaSim and Spyder to communicate must be opened. This is done by first creating a child script (Add > Associated customization script > Non Threaded) and copying the following to be the first line of code in it. 
  
  simRemoteApi.start(19999)
  
Now the code for the simulation can be written.

### Coding

The following are the steps and explanations for each section of code.
  
  - Open "TwoPlanarManipulator.py"
  - Read through the code
  - Lines 25-27: The necessary libraries to the run the code are imported. Make sure all referred libraries (sim.py, simConst.py, remoteApi.dll) are located in the same folder as the .py and .ttt files.
  - Lines 29-44: Communication with CoppeliaSim is opened. Once this is opened, all object handles are stored and displayed, so the connection is verified.
  - Lines 46-58: The object handles are stored and assigned to variable names.
  - Lines 72-88: All manipulator paramters are defined and all conversions are completed.
  - Lines 90-104: Utilizes the forward kinematics solution. The change in coordinate systems affects this part of the code.
  - Lines 109-118: Communicate the values back to CoppeliaSim to move the joints accordingly. A loop was implemented with a 1% change, so a smooth simulation was sent instead of the manipulator automatically being sent to the target location.
  - Line 120: Printing the forward kinemaitcs solution to compare back to the Dummy location to validate results. Results are validates at the following was printed: "The end effectors calculated x-position is 0.8397, and z-position is 1.4544". This matches the Dummy position as seen in the following figure.
  
| Dummy Position |
| :------------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20o%20-%20Simulation%20-%20LocationConfirmation.PNG" width="800"> |
