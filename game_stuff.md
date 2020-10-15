## Attack Done
	dmg done = determined by pstats.atk
	critnum = round(self.agility/30)
	default crit = 1/20 chance = 5%
	crit = pstats.atk*1.15
	if random.randint(1, (20-critnum)) == 1: crit else normal dmg

  
  
## pstats class 
```python
class PlayerStats():
	def __init__(self, hp : int, def : int, attack : int, agility : int, dung : list, location : str):
		self.hp = hp
		self.def = def
		self.atk = attack
		self.agility = agility
		self.curhp = hp
		self.dun = dung
		self.loc = location
```


## pstats initialization (for new game)
	hp = 20
	def = 15
	atk = 5
	agility: 4
	dung = [None, None, None, None etc]
	location = Green Fields
	curhp for battles, functions will be made in the class to calculate curhp
	
## class PlayerAssets
```python
class PlayerAssets():
	def __init__(self, gold : int, gear : list, inventory : list):
		self.gold = gold
		self.gear = gear
		self.inv = inventory
```
	
## playerassets initialization
	gold = 0
	gear= [None, None, None, None, None, None]
	inventory = []
	

## Dungeon List
	dungeonlist = ["The lost pit", "Cave of Horrors", "Divildeia Dungeon", The Dungeon of The Lost Norse Gods", "Dungeon of Nihilveia"]

## Player gear sorting:
	indexes - gearname
	0 - weapon (staff, sword, bow, orbs)
	1 - second weapon (similar to first weapon slot but has some sort of prerequisite to be used)
	2 - helmet
	3 - chestplate
	4 - leggings
	5 - boots
	6 - amulet
	7 - ring
	8 - custom


## Monsters (monster dicts will be in order of  ('name':multiplier)) :
	greenfieldmob = {'zombie':1, 'boar':1, 'slime':1, 'giant frog':2, 'slithery snake':1, 'frenzy cow' : 2}
	rabbit_islandmobs = {'killer rabbit' : , 'giant rabbit', 'evil easter bunny', 'bad hare', 'corrupted bunny'}
	valleyofdeathmob = ['skeleton', 'undead', 'giant earth worm', 'scorpio gigantia', 'evil bandits', 'horsemen']
