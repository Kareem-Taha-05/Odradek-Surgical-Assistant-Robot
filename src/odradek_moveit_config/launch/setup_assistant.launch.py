from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_setup_assistant_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("odradek_surgical_assistant", package_name="odradek_moveit_config").to_moveit_configs()
    return generate_setup_assistant_launch(moveit_config)
