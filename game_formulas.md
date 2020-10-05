## Attack Done:
	dmg done = determined by pstats.atk
	crit = 1/3 chance = 33%
	crit = pstats.atk/100*115
	

  
  
## pstats class 
```python
class Player():
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
### start stats:
`hp = 20
def = 15
atk = 5
agility: 4
dung = [None, None, None, None etc]
location = Green Fields
curhp for battles, functions will be made in the class to calculate curhp`
