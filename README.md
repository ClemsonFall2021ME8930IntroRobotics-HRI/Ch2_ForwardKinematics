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
  
Open the "TwoPlanarManipulator_Simulation.ttt" file. For this problem, we create the manipulate with two main add actions: "Add > Primitive Shape >  Cuboid" for the linkages and "Add > Joint > Revolute" for the joints.
<img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20b%20-%20Simulation%20-%20AddCuboid.PNG" width="100">
<img src="https://github.com/ClemsonFall2021ME8930IntroRobotics-HRI/Ch2_ForwardKinematics/blob/main/Figure%202.15%20c%20-%20Simulation%20-%20AddRevolute.PNG" widht="100">
  
Set the length of link 1 to 1 by keeping the x and y variables at 0.1 and changing the z variable to 1.

### Coding


