import socket
import threading
import time

# IP and port of Tello  
tello1_address = ('192.168.0.104', 8889)
tello2_address = ('192.168.0.101', 8889)

local1_address = ('', 9010)
local2_address = ('', 9011)

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.bind(local1_address)
sock2.bind(local2_address)

# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  try:
    sock1.sendto(message.encode(), tello1_address)
    sock2.sendto(message.encode(), tello2_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    try:
      response1, ip_address = sock1.recvfrom(128)
      response2, ip_address = sock2.recvfrom(128)
      print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
    except Exception as e:
      sock1.close()
      sock2.close()
      print("Error receiving: " + str(e))
      break

receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

send("command", 3)
send("battery?", 5)

send("takeoff", 8) 

send("up 80", 5) 

send("left 40", 4) 

send("down 80", 5) 

send("left 40", 4) 

send("up 80", 5) 

send("land", 2) 

print("Mission completed")

# Close the socket
sock1.close()
sock2.close()