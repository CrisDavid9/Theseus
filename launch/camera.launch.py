import os

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node (
            package='usb_cam',
            executable='usb_cam_node_exe',
            output='screen',
            parameters=[{'image_wdith': 640, 'image_height': 480, 'camera_frame_id': 'camera_link_optical'}]
        )
    ])