import time
import random
import platform

def sysinfo(): #Get local user name for the welcome message
	uname=platform.uname()
	print(f"Hallo {uname.node}! Schön, dass du hier bist! Das ist dein zufälliger Motivationsspruch: ")
def quote():
	datenbank = open ("data.txt","r")
	zeilen_einlesen = datenbank.readlines()
	zitat = random.choice(zeilen_einlesen)
	print(zitat)
	datenbank.close()

if __name__== "__main__":
	time.sleep(0.3)
	sysinfo()
	time.sleep(2)
	quote()
<<<<<<< HEAD
	time.sleep(15)
=======
	time.sleep(10)
>>>>>>> f5dedb43804293fcaab73c3541923555223a804b
