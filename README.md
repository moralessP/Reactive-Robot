
## Directory structure

./
├── mp23                  <br />
│   ├── config            <br />
│   ├── description       <br />
│   ├── launch            <br />
│   ├── worlds            <br />
│   ├── CMakeLists.txt <br />
│   ├── package.xml <br />
├── wall_follower         <br />
│   ├── launch            <br />
│   ├── scripts           <br />
│   ├── CMakeLists.txt<br />
│   ├── package.xml<br />
├── README.txt             <br />
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


