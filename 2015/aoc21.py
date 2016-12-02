# Name, Cost, Damage, Armor
weapons =[
 {'name':'Dagger','cost':8,'damage':4,'armor':0},
 {'name':'Shortsword','cost':10,'damage':5,'armor':0},
 {'name':'Warhammer','cost':25,'damage':6,'armor':0},
 {'name':'Longsword','cost':40,'damage':7,'armor':0},
 {'name':'Greataxe','cost':74,'damage':8,'armor':0}]

armors = [
 {'name':'None','cost':0,'damage':0,'armor':0},
 {'name':'Leather','cost':13,'damage':0,'armor':1},
 {'name':'Chainmail','cost':31,'damage':0,'armor':2},
 {'name':'Splintmail','cost':53,'damage':0,'armor':3},
 {'name':'Bandedmail','cost':75,'damage':0,'armor':4},
 {'name':'Platemail','cost':102,'damage':0,'armor':5}]

rings = [
 {'name':'None','cost':0,'damage':0,'armor':0},
 {'name':'None','cost':0,'damage':0,'armor':0},
 {'name':'Damage +1','cost':25,'damage':1,'armor':0},
 {'name':'Damage +2','cost':50,'damage':2,'armor':0},
 {'name':'Damage +3','cost':100,'damage':3,'armor':0},
 {'name':'Defense +1','cost':20,'damage':0,'armor':1},
 {'name':'Defense +2','cost':40,'damage':0,'armor':2},
 {'name':'Defense +3','cost':80,'damage':0,'armor':3}]

# HP, D, A
playerhp = 100
boss = {'hp':109,'damage':8,'armor':2}

def simulate(player, boss):
	p = player['hp']
	b = boss['hp']

	while True:
		b -= max(1, player['damage'] - boss['armor'])
		if b <= 0:
			return True
		p -= max(1, boss['damage'] - player['armor'])
		if p <= 0:
			return False


		

victorycost = []
losscost = []

for w in weapons:
	for a in armors:
		for r1 in rings:
			for r2 in rings:
				if (r1['name'] != 'Name' and r1 == r2):
					continue

				cost = w['cost']+a['cost']+r1['cost']+r2['cost']
				damage = w['damage']+a['damage']+r1['damage']+r2['damage']
				armor = w['armor']+a['armor']+r1['armor']+r2['armor']
				result = simulate( {'hp':playerhp, 'armor':armor, 'damage':damage}, boss )
				if (result):
					victorycost.append(cost)
				else:
					losscost.append(cost)


print('cheapest win: ' + str(min(victorycost)))
print('expensive loss: ' + str(max(losscost)))
