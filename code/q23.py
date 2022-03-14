from wlkata_mirobot import WlkataMirobot, WlkataMirobotTool
from time import sleep


arm = WlkataMirobot(portname='COM3')
arm.home()

p_a = {'x': 155.6, 'y': -115, 'z': -39.3}
p_b = {'x': 115.6, 'y': 160, 'z': -44.3}
angles_b = {
    1: 55,
    2: 65,
    3: 5,
    4: 5,
    5: -60,
    6: 0,
}

# arm.set_tool_pose(**p_a)
# arm.set_joint_angle(angles_b)

# arm.p2p_interpolation(**p_a)
# sleep(2)
# arm.p2p_interpolation(**p_b)

# arm.linear_interpolation(**p_a)
# sleep(2)
# arm.linear_interpolation(**p_b)

# arm.set_door_lift_distance(100)
# arm.set_tool_pose(**p_a)
# sleep(2)
# arm.door_interpolation(**p_b)

# arm.set_tool_pose(**p_a)
# sleep(2)
# arm.circular_interpolation(p_b['x'] - p_a['x'], p_b['y'] - p_a['y'], 250, is_cw=False)

# block_joint = {i + 1: x for i, x in enumerate([0, 31.3, 23.9, 0, -55.3, 0])}
block_joint = {i + 1: x for i, x in enumerate([0, 45.3, 23.9, 0, -55.3, 0])}
lift_joint = {i + 1: x for i, x in enumerate([0, 11.3, 23.9, 0, -55.3, 0])}

# arm.set_tool_type(WlkataMirobotTool.GRIPPER)
# arm.gripper_open()
# arm.set_joint_angle(block_joint)
# sleep(1)
# arm.set_gripper_spacing(2)
# sleep(2)
# arm.set_joint_angle(lift_joint)

arm.set_tool_type(WlkataMirobotTool.FLEXIBLE_CLAW)
arm.pump_suction()
arm.set_joint_angle(block_joint)
sleep(1)
# arm.pump_blowing()
# sleep(2)
arm.set_joint_angle(lift_joint)
