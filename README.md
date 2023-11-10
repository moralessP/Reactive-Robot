
## Directory structure

./
├── mp23                  # Package for My Robot Model<br />
│   ├── config            # Configuration Files (e.g., joint configurations)<br />
│   ├── description       # Robot's URDF Description Files<br />
│   ├── launch            # Launch Files to Spawn mp23 in Gazebo, RViz, and Robot State Publisher<br />
│   ├── worlds            # Custom World Files<br />
│   ├── CMakeLists.txt
│   ├── package.xml
├── wall_follower         # Package for My Wall-Following Algorithm<br />
│   ├── launch            # Launch Files for Running the Scripts<br />
│   ├── scripts           # Algorithm Scripts for Wall Following<br />
│   ├── CMakeLists.txt<br />
│   ├── package.xml<br />
├── README.txt             # Project Documentation<br />
./


## Requirements 

ROS neotic full package <br />
pyhton3 <br />

## How to compile

~/catkin_ws/src/wall_follower/scripts$ chmod +x main.py <br />
~/catkin_ws$ source devel/setup.bash <br />
~/catkin_ws$ catkin_make <br />

## How to execute 

~/catkin_ws$ roslaunch mp23 gazebo.launch <br />
~/catkin_ws$ roslaunch wall_follower main.launch <br />


