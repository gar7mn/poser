import bosdyn.client as client
import bosdyn.client.time_sync
import bosdyn.util as util
from bosdyn.client import  point_cloud,map_processing
from bosdyn.client.robot_command import RobotCommandBuilder,RobotCommandClient,blocking_stand
from bosdyn.client import  lease
from bosdyn.geometry import EulerZXY

class Poser:
    def __init__(self,sdk,IP,name):
        #try to create sdk
        self.sdk = client.create_standard_sdk(client_name_prefix="spot",service_clients=None)
        #create robot object
        self.robot = sdk.create_robot(IP,name=name)
        #authenticate
        self.robot.authenticate(username="user2",password="simplepassword",timeout=None)
        #lease
        self.spot_lease = self.robot.ensure_client(service_name=lease.LeaseClient.default_service_name())
        #power on robot
        with bosdyn.client.lease.LeaseKeepAlive(lease_client=self.spot_lease,lease_wallet=None,must_acquire=True,return_at_exit=True):
            self.robot.power_on(timeout_sec=30)

    def stand(self):
        try:
            bosdyn.client.robot_command.blocking_stand(command_client=self.sdk,timeout_sec=15)
        except Exception as ex:

            print(ex)


    def sit(self):
        #tell robot to sit
        sit = RobotCommandBuilder.synchro_sit_command()
        RobotCommandClient.robot_command(sit)

    def twist(self,yaw_value,roll_value,pitch_value):
         eu = EulerZXY(yaw=yaw_value,roll=roll_value,pitch=pitch_value)
         #create the pose
         pose = RobotCommandBuilder.synchro_stand_command(params=eu)
         RobotCommandClient.robot_command(pose)


    def stand_tall(self,height):
        #tell robot to stand tall.
        stand_height = RobotCommandBuilder.synchro_stand_command(body_height=height)
        RobotCommandClient.robot_command(stand_height)

    def normal_stand(self):
        #define normal stand
        stand = RobotCommandBuilder.synchro_stand_command()
        RobotCommandClient.robot_command(stand)



