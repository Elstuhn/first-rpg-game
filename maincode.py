import pickle
import os
import shutil
import sys
import random
import typing
curdir = os.getcwd()
gamefile = curdir+'/adventurefile'
swordmessage = ["You swung your sword as hard as possible at the monster.", "You thrusted your sword into the monster.", "You slashed the monster"]
bowmessage = ["You pulled the string as far back as possible and the arrow pierces the monster.", "You shot the monster in the head.", "You took an arrow and stabbed the monster."]
staffmessage = ["You cast a fireball spell at the monster.", "You cast electricity and electrocuted the monster.", "You cast an explosion spell on the monster and exploded it."]
mobmessage = ["The monster charges at you", "The monster attacks you.", "The monster ferociously attacks!", "The monster strikes you"]

class gameassets():
	def __init__(self, locmobs, locations, dungeons):
		self.locmob = locmobs
		self.locats = locations
		for _ in self.locmob:
			if pstats.loc.split()[0].lower() in _.lower():
				self.mobs = self.locmob[_]
				
	def randmob(self) -> Mob:
		mob = random.choice(list(self.mobs)) #turns self.mob into a list and picks a random key
		stats = ['hp', 'atk', 'def', 'agility']
		count = 0
		for i in stats:
			stat = eval(f"random.randint(pstats.{i}*0.95, pstats.{i}*1.05)")
			stat *= self.mobs[mob]
			stats[count] = stat
			counnt += 1
		#mobs will have plus minus 5% of player stats
		return Mob(mob, *stats) 
	
	def changelocation(self):
		for _ in self.locmob:
			if pstats.loc.split()[0].lower() in _.lower():
				self.mobs = self.locmob[_]
			
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

		equipmentid = gear_id[gearequip][0]
		#equipmentid access gear_id dictionary to retrieve string form of equipment's id
		for i in self.gear:
			if gearid[i][0] == equipmentid:
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
			
	def showinv(self):
		print("Item Number | Item Name | Item Amount")
		for num, item in enumerate(self.inv):
			print(f"{num} | {item[0]}  x{item[1]}")

class PlayerStats():
	def __init__(self, hp : int, def : int, attack : int, agility : int, dungeon : list, location : str):
		self.hp = hp
		self.def = def
		self.atk = attack
		self.agility = agility
		self.curhp = hp
		self.dun = dungeon
		self.loc = location
		
	def dmgtake(self, health : int):
		self.curhp -= health
		if self.curhp <= 0:
			moneylost = random.randint(passets.gold*0.2, passets.gold*0.35)
			print(f"You passed out and lost {moneylost}!")
			passets.gold -= moneylost
			print("You were sent to the nearest village and revived.")
			self.curhp = self.hp
			return True
		else:
			return False
		
	def heal(self, plus : int):
		if plus == None:
			self.curhp = self.hp
		else:
			self.curhp += plus
		
	def dmgdone(self):
		critminus = round(self.agility/20)
		critrand = random.randint(1, (20-critminus))
		if critrand == 1:
			dmgdone = self.atk*1.15
		else:
			dmgdone = self.atk
		return dmgdone
		
	def dunupdate(self, dungeon_number : int):
		self.dun[dungeon_number] = True

class Mob():
	def __init__(self, name : str, hp : int, atk : int, def : int, agility : int):
		self.name = name
		self.hp = hp
		self.atk = atk
		self.def = def
		self.agility = agility
		
	def dmgtake(self, dmg):
		self.hp -= dmg
		if self.hp <= 0:
			return True
		else:
			return False
	
	def dmgdone(self):
		critminus = round(self.agility/20)
		critrand = random.randint(1, (20-critminus))
		if critrand == 1:
			dmgdone = self.atk*1.15
		else:
			dmgdone = self.atk
		return dmgdone
		

def travel():
	while True:
		print("Locations:")
		for locations in gassets.locats:
			print(locations)
		location = input("Where would you like to travel to?\n")
		if not location in gassets.locats:
			print("\nInvalid location...")
			continue
		elif location == pstats.loc:
			print(f"You are already in {location}!")
			continue
		pstats.loc = location
		gassets.changelocation()
		break
	print(f"\nTravelled to {location}!")
	return f"Travelled to {location}"
			
		

def clearscreen():
	print("\n"*35)

def battle():
	#player turn
	weapon = gear_id[pstats.gear[0]][1] #Gets the weapon type of current equipped weapon
	if weapon == "sword":
		message = swordmessage
	elif weapon == "bow":
		message = bowmessage
	else:
		message = staffmessage
#Generation of hp, atk, def and agility for monster encounters are naively based on percentages of player stats
	mob = gassets.randmob() #Returns a Mob class instance
	while True:
		playermove = input("Would you like to:\n1.Attack\n2.Inventory\n3.Run\n")
		if playermove not in [1, 2, 3]:
			continue
		elif playermove == 3:
			randnum = random.randint(1, 3)
			if randnum == 1:
				print("You have successfully ran away!")
				return "Ran Away"
			else:
				print("You tripped on a rock and fell!")
				continue
				
		elif playermove == 1:
			dmgdone = pstats.dmgdone()
			mobtake = mob.dmgtake(dmgdone)
			print(random.choice(message))
			if dmgdone != pstats.atk:
				print("Critical Hit!")
			print(f"You have dealt {dmgdone} damage to {mob.name}")
			#If win
			if mobtake:
				print(f"You have defeated the {mob.name}!")
				
				return
		
		else:
			passets.showinv()
			choice = input("What would you like to do?\nType in the item number you want to use or just press enter to cancel\n") 
			while any([
				choice != "",
				not choice in item_assets
			]):
				print("Invalid Input.")
				choice = input("What would you like to do?\nType in the item number you want to use or just press enter to cancel\n") 
			item = pstats.inv[choice]
			consume(item[0])
			if item[1] >1:
				pstats.inv[choice][1] -= 1
			else:
				del pstats.inv[choice]
		#Mob turn
		dmgdone = mob.dmgdone()
		print(random.choice(mobmessage))
		if dmgdone != mob.atk:
			print("Critical Hit!")
		print(f"The {mob.name} deals {dmgdone} to you!")
		ptake = pstats.dmgtake(dmgdone)
		if ptake:
			return
		
			
		
		
		
def consume(item):
	returnlis = []
	stats = item_assets[item]
	stats = stats.split()
	for i in stats:
		i = i.split(":")
		pstats.i[0] += int(i[1])
		returnlis.append([i[0], i[1]])
	return returnlis
		
def unconsume(lis):
	for i in lis:
		if i[0] != "hp":
			pstats.i[0] -= i[1]
		else:
			continue
	
def tutorial():


def initialize():
	open(gamefile+'/playerassets', 'x')
	open(gamefile+'/gameassets', 'x')
	open(gamefile+'/playerstats', 'x')
	open(gamefile+'/playerassets', 'x').close()
	open(gamefile+'/playerstats', 'x').close()
	open(gamefile+'/gameassets', 'x').close()
	'''gamefiles has been made, to speed things up, we will not load game data if they had created a new game
	thus, player data and assets will need to be initialized, everything being initialized will be empty'''
	pstats = PlayerStats(20, 15, 5, 4, [None, None, None, None, None], "Green Fields")
	#there are 5 dungeons, uncompleted dungeons will be counted as none
	passets = PlayerAssets(0, [None, None, None, None, None, None, None, None], [])
	allmob = {
		greenfieldmob : {'zombie':1, 'boar':1, 'slime':1, 'giant frog':1.2, 'slithery snake':1, 'frenzy cow' : 1.1},
		rabbit_islandmobs : {'killer rabbit' : 1.2, 'giant rabbit' : 1.1, 'evil easter bunny' : 1.2, 'bad hare' : 1, 'corrupted bunny' : 1, "Psychotic Hare" : 1.3},
		valleyofdeathmob : {'skeleton' : 1, 'undead' : 1.1, 'giant earth worm' : 1.3, 'scorpio gigantia' : 1.4, 'evil bandits' : 1.1, 'horsemen' : 1.2}
			 }
	#Locations will go in a descending order from easiest to hardest location
	
			  #The minimum multiplier will always be 1
	locations = ["Green Field", "Rabbit Islands", "Valley of Death"]
	dungeons = ["The lost pit", "Cave of Horrors", "Divildeia Dungeon", "The Dungeon of The Lost Norse Gods", "Dungeon of Nihilveia"]
	gassets = gameassets(allmob, locations, dungeons)
	

def savegame():
	with open(gamefile+'/playerassets', 'wb') as writefile:
		pickle.dump(passets, writefile)
		
	with open(gamefile+'/playerstats', 'wb') as writefile:
		pickle.dump(pstats, writefile)
	#playerstats will be a PlayerStats instance 
			  
	with open(gamefile+'/gameassets', 'wb') as writefile:
		pickle.dump(gassets, writefile)
	
def load_game():
	with open(gamefile+'/playerassets', 'rb') as readfile:
		passets = pickle.load(readfile)
	with open(gamefile+'/playerstats', 'rb') as readfile:
		pstats = pickle.load(readfile)
	with open(gamefile+'/gameassets', 'rb') as readfile:
		gassets = pickle.load(readfile)
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
