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
        
        # Indítjuk a hexagon_turtle node-ot
        Node(
            package='bag_njb',  #
            executable='hexagon_turtle',  
            name='hexagon_turtle',  
            output='screen'  
        )
    ])
