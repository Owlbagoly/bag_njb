from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='bag_njb',  # Az általad megadott csomag neve
            executable='project_node.py',  # Az indítani kívánt végrehajtható fájl
            output='screen',
        ),
    ])
