## Attack Done:
	dmg done = determined by pstats.atk
	crit = 1/3 chance = 33%
	crit = pstats.atk/100*115
	

  
  
## pstats class 
class Player():
	def __init__(self, hp : int, def : int, attack : int, dung : list):
		self.hp = hp
		self.def = def
		self.atk = attack
		self.curhp = hp
		self.dun = dung

### Class for pstats instance
start stats:
hp = 20
def = 15
atk = 5
agility: 4
dung = [None, None, None, None etc]
location = Green Fields
curhp for battles, functions will be made in the class to calculate curhp 