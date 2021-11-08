from djitellopy import Tello


me = Tello()
me.connect()

print(me.get_battery())

me.connect_to_wifi(ssid="TP-Link_Caguama", password="Dermochelys1") # Nombre de la red y contraseña



