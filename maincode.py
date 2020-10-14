import pickle
import os
import shutil
import sys
import random
import typing
curdir = os.getcwd()
gamefile = curdir+'/adventurefile'

class locmob():
	def __init__(self, locmobs):
		self.locmob = locmobs
		for _ in self.locmob:
			if pstats.loc.split()[0] in _:
				self.mobs = self.locmob[_]
				
	def randmob(self):
		mob = random.choice(list(self.mobs)) #turns self.mob into a list and picks a random key
		stats = ['hp', 'atk', 'def', 'agility']
		count = 0
		for i in stats:
			stats[count] = eval(f"random.randint(pstats.{i}*0.95, pstats.{i}*1.05)")
			counnt += 1
		#mobs will have plus minus 5% of player stats
		return Mob(mob, *stats) 

class PlayerAssets():
	def __init__(self, gold : int, gear : list, inventory : dict):
		self.gold = gold
		self.gear = gear
		self.inv = inventory
	
	def equip(self, num : int):
#num is the number of the equipment in the inventory
#inventory will be enumerated so order will start from 0
		try:
			gearequip = self.inv[num][0]
		except:
			return "Error | Item position not found."
		if not gearequip in gear_list:
			return "Sorry, you cannot equip that!"
		elif gearequip in self.gear:
			return "You already have that equipped!"

		equipmentid = gear_id[gearequip]
		#equipmentid access gear_id dictionary to retrieve string form of equipment's id
		for i in self.gear:
			if gearid[i] == equipmentid:
		#gearid[i] has a possibility of being None therefore gearid[None] will be hashmapped to -1
				ver = input(f"Would you like to unequip {self.gear(equipmentid)} to equip {gearequip}? (yes/no)\n")
				while not ver.lower() in ['yes', 'no']:
					ver = input(f"Would you like to unequip {self.gear(equipmentid)} to equip {gearequip}? (yes/no)\n")
				if ver.lower() == 'no':
					return
            
		gearunequip = self.gear.pop(equipmentid)
		gearequip = self.inv[num][0]
		self.gear[equipmentid] = gearequip
		equipnum = self.inv[num][1]
		if equipnum>1:
			self.inv[num][1] -=1
		else:
			del self.inv[num]
			#equipment ids correlate with pgear index
		for _ in self.inv:
			if gearunequip in _:
				_[1] +=1
				return f"Equipped {gearequip}!"		
		self.inv.append([gearunequip, 1])
		return f"Equipped {gearequip}!"	
			

class PlayerStats():
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
		critminus = round(self.agility/20)
		random = random.randint(1, (20-critminus))
		if random == 1:
			dmgdone = self.atk*1.15
		else:
			dmgdone = self.atk
		return dmgdone
		
	def dunupdate(self, dungeon_number : int):
		self.dung[dungeon_number] = True

class Mob():
	def __init__(self, name : str, hp : int, atk : int, def : int, agility : int):
		self.name = name
		self.hp = hp
		self.atk = atk
		self.def = def
		self.agility = agility
		
	def dmgtake(self, dmg):
		self.hp -= dmg
		if self.hp <= 1:
			return True
		else:
			return False
		

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
	open(gamefile+'/playerassets', 'x')
	open(gamefile+'/mobassets', 'x')
	open(gamefile+'/playerstats', 'x')
	open(gamefile+'/playerassets', 'x').close()
	open(gamefile+'/playerstats', 'x').close()
	open(gamefile+'/mobassets', 'x').close()
	'''gamefiles has been made, to speed things up, we will not load game data if they had created a new game
	thus, player data and assets will need to be initialized, everything being initialized will be empty'''
	pstats = PlayerStats(20, 15, 5, 4, [None, None, None, None, None], "Green Fields")
	#there are 5 dungeons, uncompleted dungeons will be counted as none
	passets = PlayerAssets(0, [None, None, None, None, None, None, None, None], [])
	massets = locmob()
	

def savegame():
	with open(gamefile+'/playerassets', 'wb') as writefile:
		pickle.dump(passets, writefile)
		
	with open(gamefile+'/playerstats', 'wb') as writefile:
		pickle.dump(pstats, writefile)
	#playerstats will be a PlayerStats instance 
			  
	with open(gamefile+'/mobassets', 'wb') as writefile:
		pickle.dump(massets, writefile)
	
def load_game():
	with open(gamefile+'/playerassets', 'rb') as readfile:
		passets = pickle.load(readfile)
	with open(gamefile+'/playerstats', 'rb') as readfile:
		pstats = pickle.load(readfile)
	with open(gamefile+'/mobassets', 'rb') as readfile:
		massets = pickle.load(readfile)
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
		ver = input("Are you sure you want to create a new game?\nThis will wipe out your existing save files (yes/no)\n")
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
		time.sleep(5)

