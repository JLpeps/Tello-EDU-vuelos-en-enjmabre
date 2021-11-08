from djitellopy import Tello


me = Tello()
me.connect()

print(me.get_battery())

me.connect_to_wifi(ssid="TP-Link_Caguama", password="D3rmoch3lys%1")



