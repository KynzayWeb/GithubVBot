import requests
from os import system
from pystyle import *
import threading
import os

os.system('title ๐๐ข๐ญ๐ก๐ฎ๐๐๐๐จ๐ญ By Nity Web#0666')
os.system('cls')
os.system('mode 60, 16')

print(Colorate.Horizontal(Colors.blue_to_purple , """\n
				 โโ โข โช  โโโโโ โ .โโโข โโโโโโยท  โ โยทโโโโยท       โโโโโ
				โโ โ โชโโ โขโโ  โโโชโโโโชโโโโโ โโโชโชโยทโโโโ โโโชโช     โขโโ  
				โโ โโโโโยท โโ.โชโโโโโโโโโโโโโโโโโโโโโขโโโโโโ โโโโ  โโ.โช
				โโโโชโโโโโ โโโยทโโโโโโโโโโโโโโชโโ โโโ โโโโชโโโโโ.โโ โโโยท
				ยทโโโโ โโโ โโโ โโโ ยท โโโ ยทโโโโ . โ  ยทโโโโ  โโโโโช โโโ 
        
""" ,1 ))
print(Colors.blue + '       		https://github.com/kynzayweb\n' + Colors.reset)

choice = input(Colors.purple + "		[" + Colors.blue + "1" + Colors.purple + "]" + Colors.gray + " profile-counter.glitch.me\n" + Colors.purple + "		[" + Colors.blue + "2" + Colors.purple +"]" + Colors.gray + " gpvc.arturio.dev\n<User/> ")
system("cls")
username = input(Colors.purple + "	[" + Colors.blue + "1" + Colors.purple + "]" + Colors.gray + " username\n> ")
system("cls")
amount = int(input(Colors.purple + "	[" + Colors.blue + "1" + Colors.purple + "]" + Colors.gray + " amount\n> "))
counter = 0


def profile():
	global username
	r = requests.get(f"https://profile-counter.glitch.me/{username}/count.svg")

def gpvc():
	global username
	r = requests.get(f"https://gpvc.arturio.dev/{username}")

if choice == "1":
	for i in range(amount, 0, -1):
		thread = threading.Thread(target=profile)
		thread.start()
		counter +=1
		system("cls")
		print(f"{counter}/{amount}")
elif choice == "2":
	for i in range(amount, 0, -1):
		thread = threading.Thread(target=gpvc)
		thread.start()
		counter +=1
		system("cls")
		print(f"{counter}/{amount}")	
