import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node (
            package='412_camera',
            executable='v412_camera_node',
            output='screen',
            parameters=[{'image_size': [640,480], 'camera_frame_id': 'camera_link_optical'}]
        )
    ])