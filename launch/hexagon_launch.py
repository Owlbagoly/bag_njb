import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Indítjuk a turtlesim node-ot
        Node(
            package='turtlesim',  
            executable='turtlesim_node',  
            name='turtlesim',  
            output='screen'  
        ),
        
        # Indítjuk a project_node node-ot
        Node(
            package='bag_njb',  #
            executable='project_node',  
            name='project_node',  
            output='screen'  
        )
    ])
