from Poser import Poser

def main():
    Bucky = Poser(sdk="poser",IP="192.168.80.3",name="Bucky")
    Bucky.stand()
    Bucky.twist(yaw_value=0.0,roll_value=0.0,pitch_value=0.2)
    Bucky.normal_stand()
    Bucky.sit()
main()