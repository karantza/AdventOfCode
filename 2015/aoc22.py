from copy import copy, deepcopy
from random import shuffle

bossStats = {'hp':58, 'damage':9}

spells = [
{'name':'M', 'cost':53, 'damage':4, 'heal':0, 'effect':None},
{'name':'D', 'cost':73, 'damage':2, 'heal':2, 'effect':None},
{'name':'S', 'cost':113, 'damage':0, 'heal':0, 'effect':{'timer':6, 'name':'S'}},
{'name':'P', 'cost':173, 'damage':0, 'heal':0, 'effect':{'timer':6, 'name':'P'}},
{'name':'R', 'cost':229, 'damage':0, 'heal':0, 'effect':{'timer':5, 'name':'R'}}]

playerStats = {'hp':50, 'mana':500, 'armor':0}

hardmode = True

def myprint(x):
	#print(x)
	return

def applyEffect(boss, player, effect):

	if effect['name'] == 'P':
		myprint('Poison deals 3 damage')
		boss['hp'] -= 3
	elif effect['name'] == 'R':
		myprint('Recharge provides 101 mana')
		player['mana'] += 101

	effect['timer'] -= 1
	myprint(effect['name'] + "'s timer is now " + str(effect['timer']))
	return (effect['timer'] == 0)

def castSpell(boss, player, spell, effects):

	myprint("Casting spell " + spell['name'])

	boss['hp'] -= spell['damage']
	player['hp'] += spell['heal']

	effect = copy(spell['effect'])

	if effect:
		if effect['name'] == 'S':
			myprint("Shields increases armor by 7")
			player['armor'] += 7
		effects.append(effect)
	return spell['cost']

victories = []
losses = []

def applyEffects(boss,player,effects):
	# Apply effects, and tell us which have expired

	expired = []

	for e in effects:
	 if applyEffect(boss, player, e):
	 	expired.append(e)

	for e in expired:
		if (e['name'] == 'S'):
			myprint('Sheild wears off, armor drops by 7')
			player['armor'] -= 7
		myprint('Removing effect ' + e['name'])
		effects.remove(e)


def takeTurns(boss, player, spell, effects, spent, history):	

	if (hardmode):
		player['hp'] -= 1

		if (player['hp'] <= 0):
			myprint("Player loses with " + str(spent) + ", " + history)
			#losses.append(spent)
			return (spent,history)

	#Player's turn
	myprint('')
	myprint("-- Player turn --")
	myprint("- Player has " + str(player['hp']) + " hp, " + str(player['armor']) + " armor, " + str(player['mana']) + " mana")
	myprint("- Boss has " + str(boss['hp']) + " hp")

	applyEffects(boss,player,effects) # Apply existing effects

	activeEffects = map(lambda x: x['name'], effects)
	if spell['cost'] > player['mana']:
		# Can't cast this spell :(
		return
	if len(victories) > 0 and spell['cost'] + spent > min(victories):
		# Not worth looking, too expensive
		return
	if spell['name'] in activeEffects:
		# Can't cast, already active
		return

	cost = castSpell(boss, player, spell, effects) # Cast prepared spell
	spent += cost
	player['mana'] -= cost
	history += spell['name']
	myprint("player has spent " + str(spent) + " on " + history)

	if (boss['hp'] <= 0):
		print("Player wins with " + str(spent) + ", " + history)
		victories.append(spent)
		return (spent,history)

	# Boss's turn
	myprint("-- Boss turn --")
	myprint("- Player has " + str(player['hp']) + " hp, " + str(player['armor']) + " armor, " + str(player['mana']) + " mana")
	myprint("- Boss has " + str(boss['hp']) + " hp")

	applyEffects(boss,player,effects) # Apply existing effects

	damage = max(1, boss['damage'] - player['armor'])

	player['hp'] -= damage

	myprint('Boss does ' + str(damage) + " damage, player at " + str(player['hp']))

	if (player['hp'] <= 0):
		myprint("Player loses with " + str(spent) + ", " + history)
		#losses.append(spent)
		return (spent,history)
	if (boss['hp'] <= 0):
		print("Player wins with " + str(spent) + ", " + history)
		victories.append(spent)
		return (spent,history)

	activeEffects = map(lambda x: x['name'], effects)

	for s in spells:
		takeTurns(copy(boss), copy(player), s, deepcopy(effects), spent, history)
	
	return (spent,history)

def test():
	M = spells[0]
	D = spells[1]
	S = spells[2]
	P = spells[3]
	R = spells[4]
	seq = [P,M,R,P,S,R,P,D,M]
	effects = []
	spent = 0
	history = ''
	for s in seq:
		(spent,history) = takeTurns(bossStats, playerStats, s, effects, spent, history)


takeTurns(copy(bossStats),copy(playerStats),spells[0],[],0,'')
takeTurns(copy(bossStats),copy(playerStats),spells[1],[],0,'')
takeTurns(copy(bossStats),copy(playerStats),spells[2],[],0,'')
takeTurns(copy(bossStats),copy(playerStats),spells[3],[],0,'')
takeTurns(copy(bossStats),copy(playerStats),spells[4],[],0,'')

print(str(len(victories)) + " victories, " + str(len(losses)) + " losses")
print('best victory: ' + str(min(victories)))

