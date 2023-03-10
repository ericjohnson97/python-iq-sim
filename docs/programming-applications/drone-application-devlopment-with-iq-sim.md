# Drone Application Devlopment with IQ Sim

The Intelligent Quads online simulator offers an easy and straightforward way to begin writing applications. Our IQ sim client generates UDP mavlink streams that can be consumed by popular mavlink libraries, including MAVROS, pymavlink, MAVSDK, and dronekit. Whether you're an experienced developer or just starting out, our simulator streamlines the process by providing the necessary tools to begin working on your projects immediately.

### MAVlink Libraries

#### Pymavlink

Pymavlink is a library that wraps the autogenerated mavlink messages from the mavlink messages XMLs. It provides minimal high macro functions and is very closed to purely handling the communication at a protocol level. Pymavlink can be good for understanding the communcation that goes on between mavlink systems. Since pymavlink has minimal high level functionality it your application relies less on other peoples implementations of high level functions

[https://github.com/ArduPilot/pymavlink](https://github.com/ArduPilot/pymavlink)

#### MAVSDK

MAVSDK is an exciting project that provides higher level macro functions. MAVSDK is actively being maintained by the Dronecode foundation which is the foundation that oversees QGroundcontrol and works closely with the PX4 community. MAVSDK is primarily designed to work with PX4 and use with Ardupilot is a "use at your own risk" deal.&#x20;

[https://github.com/mavlink/MAVSDK](https://github.com/mavlink/MAVSDK)

#### MAVROS

MAVROS is a library that provides a translation between mavlink protocol to ROS messages. This can be a good option for developers who really want to live in a ROS enviorment. One draw back using MAVROS is that sometimes it is hard to figure out how the ROS messages translate to mavlink messages.&#x20;

[https://github.com/mavlink/mavros](https://github.com/mavlink/mavros)
