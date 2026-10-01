# Copyright 2025 Institute for Automotive Engineering (ika), RWTH Aachen University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Get package directory
    pkg_dir = get_package_share_directory('depth_anything_v3')
    

    config_file = yaml.safe_load(
        open(
            os.path.join(
                pkg_dir,
                "config",
                "depth_anything_v3.param.yaml",
            ),
            "r",
            encoding="utf-8",
        )
    )["depth_anything_v3"]

    # Depth Anything V3 node
    depth_anything_v3_node = Node(
        package='depth_anything_v3',
        executable='depth_anything_v3_main',
        name='depth_anything_v3',
        output='screen',
        parameters=[config_file["ros__parameters"]],
        remappings=[
            tuple(pair) for pair in config_file["remappings"]
        ],
    )

    return LaunchDescription([
        # Nodes
        depth_anything_v3_node,
    ])
