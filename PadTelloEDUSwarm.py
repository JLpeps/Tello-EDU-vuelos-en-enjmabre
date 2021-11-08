import socket
import threading
import time
local1_address = ('', 9010)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock1.bind(local1_address)
tello1_address = ('192.168.0.101', 8889)
local2_address = ('', 9011)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
sock2.bind(local2_address)
tello2_address = ('192.168.0.102', 8889)
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
def receive1():
  while True:
    try:
      response1, ip_address = sock1.recvfrom(128)
      print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
    except Exception as e:
      sock1.close()
      print("#1 Error receiving: " + str(e))
      break
def receive2():
  while True:
    try:
      response2, ip_address = sock2.recvfrom(128)
      print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
    except Exception as e:
      sock2.close()
      print("#2 Error receiving: " + str(e))
      break
receiveThread1 = threading.Thread(target=receive1)
receiveThread1.daemon = True
receiveThread1.start()
receiveThread2 = threading.Thread(target=receive2)
receiveThread2.daemon = True
receiveThread2.start()

send1("command", 3)
send2("command", 3)
send1("mon", 2)
send2("mon", 2)
send1("takeoff", 3)
send2("takeoff", 4)
send1("go 0 0 100 50 m2", 4) #1
send2("go 0 0 100 50 m1", 5)
send1("jump 115 0 100 50 0 m2 m3", 4) #2
send2("jump 115 0 100 50 0 m1 m2", 8)
send1("jump 115 0 100 50 0 m3 m4", 8) #3
send2("jump 115 0 100 50 0 m2 m3", 10)
send1("jump 115 0 100 50 0 m4 m5", 8) #4
send2("jump 115 0 100 50 0 m3 m4", 8)
send1("jump 115 0 100 50 0 m5 m6", 8) #5
send2("jump 115 0 100 50 0 m4 m5", 10)
send1("jump 115 0 100 50 0 m6 m7", 8) #6
send2("jump 115 0 100 50 0 m5 m6", 8)
send1("jump 115 0 100 50 0 m7 m8", 10) #7
send2("jump 115 0 100 50 0 m6 m7", 8)
send1("jump 115 0 100 50 0 m7 m8", 8) #8
send2("jump 115 0 100 50 0 m6 m7", 8)

print("Mission completed successfully!")
sock1.close()
sock2.close()
