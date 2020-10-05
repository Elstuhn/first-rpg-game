import pickle
import os
import shutil
import sys
import random
import typing
curdir = os.getcwd()
gamefile = curdir+'/adventurefile'

class Player():
	def __init__(self, hp : int, def : int, attack : int, agility : int, dung : list, location : str):
		self.hp = hp
		self.def = def
		self.atk = attack
		self.agility = agility
		self.curhp = hp
		self.dun = dung
		self.loc = location
		
	def dmgtake(self, health : int):
		self.curhp -= health
		
	def heal(self):
		self.curhp = self.hp
		
	def dmgdone(self):
		maxatk = (self.atk*2)//1.5
		dmgdone = random.randint(self.atk, maxatk)
		return dmgdone
		
	def dunupdate(self, dungeon_number : int):
		self.dung.append(dungeon_list[dungeon_number-1])

class Mob():
	def __init__(self, name : str, hp : list, atk : int, def : int, agility : int):
		self.name = name
		self.hp = hp
		self.atk = atk
		self.def = def
		self.agility = agility
		
	

greenfieldmob = [
rabbit_islandmobs = ['killer rabbit', 'giant rabbit', 'evil easter bunny', 'bad hare', 'corrupted bunny']

def travel():
	while True:
		location = input("Where would you like to travel to?")
		if not location in locations:
			print("\nInvalid location...")
			continue
		elif location == pstats.loc:
			print(f"You are already in {location}!")
			continue
		pstats.loc = location
		break
	print(f"\nTravelled to {location}!")
	return f"Travelled to {location}"
			
		

def clearscreen():
	print("\n"*35)

def battle():
#Generation of hp, atk, def and agility for monster encounters will be naively based on percentages of player stats
	if self.location == "Green Fields":
		mobchoices = greenfieldmob
	mobname = random.choice(list(mobchoices))
	mobhp = random.randint(pstats.hp/100*
	mob = Mob(mobname, 


def tutorial():


def initialize():
	open(gamefile+'/gear', 'x')
	open(gamefile+'/inventory', 'x')
	open(gamefile+'/playerstats', 'x')
	open(gamefile+'/gear', 'x').close()
	open(gamefile+'/inventory', 'x').close()
	open(gamefile+'/playerstats', 'x').close()
	'''gamefiles has been made, to speed things up, we will not load game data if they had created a new game
	thus, player data and assets will need to be initialized, everything being initialized will be empty'''
	pstats = Player(20, 15, 5, 4, [None, None, None, None, None], "Green Fields")
	#there are 5 dungeons, uncompleted dungeons will be counted as none
	pgear = [None, None, None, None, None, None, None, None]
	#pgear is sorted by gear id, thus it won't be empty instead it will be None
	pinv = []

def savegame():
	with open(gamefile+'/inventory', 'wb') as writefile:
		pickle.dump(pinv, writefile)
	#inventory will be a nested list object ([0, 0] = item(string) [0, 1] = quantity(int))
	
	with open(gamefile+'/gear', 'wb') as writefile:
		pickle.dump(pgear, writefile)
	#pgear will be a list object
		
	with open(gamefile+'/playerstats', 'wb') as writefile:
		pickle.dump(pstats, writefile)
	#playerstats will be a class instance object
		
	
def equip(num : int):
#num is the number of the equipment in the inventory
#inventory will be enumerated so order will start from 0
	try:
		pinv[num]
		gearequip = pinv[num]
		if not gearequip in gear_list:
			return "Sorry, you cannot equip that!"
		elif gearequip in pgear:
			return "You already have that equipped!"

		equipmentid = gear_id[gearequip]
		#equipmentid access gear_id dictionary to retrieve string form of equipment's id
		for i in pgear:
			gearid = gear_id[i]
			if gearid == equipmentid:
				ver = input("Would you like to unequip old gear and re-equip new gear? (yes/no)\n")
				while not ver.lower() in ['yes', 'no']:
					ver = input("would you like to unequip old gear and re-equip new gear? (yes/no)\n")
				if ver.lower() == 'no':
					return
				else:
					gearunequip = pgear.pop(equipmentid)
					if pinv[num][1]>1:
						pinv[num][1] -=1
						gearequip = pinv[num][0]
						pgear[equipmentid] = gearequip
	
					else:
						gearequip = pinv[num][0]
						del pinv[num]
						pgear[equipmentid] = gearequip
					#equipment ids correlate with pgear index
					for _ in pinv:
						if gearunequip in _:
							_[1] += 1
						else:
							pinv.append([gearunequip, 1])
			
	except:

		return "Error | Item position not found."
		
#equip function needs to be printed to show the return strings
	
def load_game():
	with open(gamefile+'/gear', 'rb') as readfile:
		pgear = pickle.load(readfile)
	with open(gamefile+'/inventory', 'rb') as readfile:
		pinv = pickle.load(readfile)
	with open(gamefile+'/playerstats', 'rb') as readfile:
		pstats = pickle.load(readfile)
	
def credits():
	print("\n\nGame Development\n-Elston\n\nDirector\n-Elston\n\nScripter\n-Elston\n\nAsset Makers\n-Elston")

def menuscreen():
	space = "|" + " "*25 + "|"
	print("-"*25)
	print(space)
	print("| 1)  New Game" + " "*12 + "|")
	print("|" + " "*25 + "|")
	print("| 2) Resume Game" + " "*12 + "|")
	print("|" + " "*25 + "|")
	print("| 3) Credits" + " "*12 + "|")
	print("-"*25)
	
bool = os.path.isdir(curdir+'/adventurefile')	

while True:
	menuscreen()
	option = input("\n\n")
	if not bool and option == '2':
		print("Error | Save file not found.\n")
		continue
	elif not option in ['1', '2', '3']:
		print("Invalid Input | Please enter a valid option given\n")
		continue
			
	if option == '1':
		ver = input("Are you sure you want to create a new game?\nThis might wipe out your existing save files (yes/no)\n")
		while not ver.lower() in ['yes', 'no']:
			ver = input("Are you sure you want to create a new game?\nThis will wipe out any of your existing save files (yes/no)\n")
		if ver.lower() == 'yes':
			try:
				os.mkdir(gamefile)
				initialize()
				
				break
			except:
				shutil.rmtree(gamefile)
				os.mkdir(gamefile)
				initialize()
				break
		else:	
			pass
	
	elif option == '2':
		load_game()
		break
	
	else:
		credits()
	
