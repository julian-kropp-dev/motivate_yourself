import time
import random
import platform
import getpass

def sysinfo(): #Get local user name for the welcome message
	uname = getpass.getuser()
	print(f"Hallo {uname}! Schön, dass du hier bist! Das ist dein zufälliger Motivationsspruch: ")
def quote():
	datenbank = open ("data.txt", "r")
	zeilenEinlesen = datenbank.readlines()
	zitat = random.choice(zeilenEinlesen)
	print(zitat)
	datenbank.close()

if __name__== "__main__":
	time.sleep(0.4)
	sysinfo()
	time.sleep(2)
	quote()
	time.sleep(15)
