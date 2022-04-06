import time
import random
#Color
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'

print(pink+"==================")
print(red+"    WELCOME                                                         TO DDOS                                                           CLARAT           ")
print(pink+"=================")
print("{1} Siap")
print("{2} Gak")
option=int(input("SIAP DDOS ? :"))

if option=='1':
   print("Gas")
#ddos
ip = input(gren+"IP :")
port =input(cyan+"PORT :")
kata ="|• PAKET•| ×BOOM ! ! PAKET !! { BY : CLARAT }\n IP/PORT× :"
for i in range(2000):
    print(b+yellow+(kata),pink+ip,":",red+port)
    time.sleep(0.11)
    print("PAKET TERKIRIM !_!_!")
    
