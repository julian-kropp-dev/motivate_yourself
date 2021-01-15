import time
import random
import platform

def sysinfo():
	uname=platform.uname()
	print(f"Hallo {uname.node}! Schön, dass du hier bist! Das ist dein zufälliger Motivationsspruch: ")
def quote():
	datenbank = open ("data.txt","r")
	zeilen_einlesen = datenbank.readlines()
	zitat = random.choice(zeilen_einlesen)
	print(zitat)
	datenbank.close()

if __name__== "__main__":
	sysinfo()
	quote()
	time.sleep(10)