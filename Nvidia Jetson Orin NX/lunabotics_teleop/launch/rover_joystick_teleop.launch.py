from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joystick"
    )

    joy_teleop = Node(
        package="joy_teleop",
        executable="joy_teleop",
        parameters=["/home/uhcl_lunabotics/lunabotics_ws/src/lunabotics_teleop/config/joy_teleop.yaml"],
    )

    return LaunchDescription([
        joy_node,
        joy_teleop
    ])
