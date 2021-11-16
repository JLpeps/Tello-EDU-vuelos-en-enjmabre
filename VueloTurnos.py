# Import the necessary modules
import socket
import threading
import time

local1_address = ('', 9010)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
sock1.bind(local1_address)
tello1_address = ('192.168.0.101', 8889)


local2_address = ('', 9011)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
sock2.bind(local2_address)

tello2_address = ('192.168.0.102', 8889)

##############################################

def send1(message, delay): #para tello1
  try:
    sock1.sendto(message.encode(), tello1_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))
  time.sleep(delay)

def send2(message, delay): #para tello2
  try:
    sock2.sendto(message.encode(), tello2_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))
  time.sleep(delay)
##############################################

def receive1():
  while True:
    try:
      response1, ip_address1 = sock1.recvfrom(128)
      print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
    except Exception as e:
      sock1.close()
      print("#1 Error receiving: " + str(e))
      break


def receive2():
  while True:
    try:
      response2, ip_address2 = sock2.recvfrom(128)
      print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
    except Exception as e:
      sock2.close()
      print("#2 Error receiving: " + str(e))
      break

###############################################

receiveThread1 = threading.Thread(target=receive1)
receiveThread1.daemon = True
receiveThread1.start()

receiveThread2 = threading.Thread(target=receive2)
receiveThread2.daemon = True
receiveThread2.start()

###############################################

send1("command", 2)
send2("command", 7)

send1("battery?", 3)
send2("battery?", 3)

send1("takeoff", 2)
send2("takeoff", 7)

send1("up 80", 4) 
send2("right 40", 3) 

send1("left 40", 3) 
send2("up 80", 3) 

send1("down 80", 3) 
send2("left 40", 3) 

send1("right 40", 3) 
send2("down 80", 3)

send1("land", 3) 
send2("land", 3) 

print("Mission completed successfully!")

sock1.close()
sock2.close()