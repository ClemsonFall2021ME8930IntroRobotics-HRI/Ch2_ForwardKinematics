# Ch2_ForwardKinematics

## Problem Statement

Finding the forward kinematic solution of a 2-link planar manipulator. Use the found soluton to wriate a phyton code and simulate in CoppeliaSim.

## Pre-requisites:

- Software: CoppeliaSim (for simulation), Spyder (for Python coding)
- Basic Python syntax
- Understanding of the python remote API commands for CoppeliaSim

## Solution

![2 link planar manipulator](https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20-%20Simulation%20-%20DH%20Examples-09.png)

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
  
Next, it must be defined on where the manipulator should go. To do this, "Add > Dummy". Add two Dummy's in and rename one of the Dummy's to be labelled as "Target". Double click on the dummy icon to bring up the "Scene Object Properties". In here, change the Linked Dummy drop down to refer to the other dummy. The below example is the Target Dummy properties, so it is being linked to the Dummy. The Dummy color can be adjusted here as well.
  
| Dummy Properties |
| :--------------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20m%20-%20Simulation%20-%20DummyProperties.PNG" width="400"> |
  
The Target Dummy is the input for the forward kinematic. It must remain in the same plane as our final link as the manipulator as we are only dealing with revolute joints to create the 2-Link Planar Manipulator. The reamining Dummy should be centered at the end of link 2.
  
It is important to make sure all the correct properties are set. For each link, double click on the cuboid logo to bring up the "Scene Object Properties". For all cuboids, stay in the "Shape" tab, click on "Show Dynamic Properties Dialog" and unselect "Body is dynamic". If this is not deselected, then the link will fall to the ground due to gravity. For the base cuboid, click on the "Common" tab and select "Object is model base". For each joint, double click on the revolute joint logo to bring up the "Scene Object Properties". For all joints, stay in the "Joint" tab and change the Mode to "Passive Mode" to enable to the joint to drive the connected link.
  
| All Cuboids Properties | Base Cuboid Properties | R Joint Properties |
| :--------------------: | :--------------------: | :----------------: |
| <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20j%20-%20Simulation%20-%20AllCuboidProperties.PNG" width="400"> | <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20k%20-%20Simulation%20-%20BaseCuboidProperties.PNG" width="300"> | <img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20l%20-%20Simulation%20-%20BaseCuboidProperties.PNG" width="300"> |
  
The last change to the objects to make is to assign the correct hierarchy. To do so, drag the child object on top of the parent object to make the hierarchy link. It should look like this:

### Coding


