from djitellopy import Tello
import time
######################################################################
width = 320  # WIDTH OF THE IMAGE
height = 240  # HEIGHT OF THE IMAGE
startCounter =0   #  0 FOR FIGHT 1 FOR TESTING
######################################################################


# CONNECT TO TELLO
me = Tello()
me.connect()

print(me.get_battery())

me.connect_to_wifi(ssid="TP-Link_Caguama", password="D3rmoch3lys%1")



