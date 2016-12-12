from collections import deque
from itertools import combinations
from copy import deepcopy
import string

checksums = set()

class Thing:
	def __init__(self, type, name):
		self.type = type
		self.name = name
		self.str = type + name[:3]

	def __repr__(self):
  		return self.str

def isFloorSafe(floor):
	for f in range(0,4):
		chips = set([x.name for x in floor[f] if x.type == "M"])
		rtgs = set([x.name for x in floor[f] if x.type == "G"])
		unpowered = chips - rtgs
		if unpowered and rtgs:
			return False
	return True

class State:
	def __init__(self, steps, e, floor):
		self.steps = steps
		self.e = e
		self.floor = floor

	def isFinished(self):
		return (len(self.floor[0]) + len(self.floor[1]) + len(self.floor[2])) == 0 and self.e == 3

	def checksum(self):
		mapping = {}
		char = 0

		c = str(self.e)
		for f in range(0,4):
			c += str(f)
			things = []
			for thing in self.floor[f]:
				if thing.name not in mapping:
					mapping[thing.name] = string.ascii_uppercase[char]
					char += 1
				things.append(thing.type + mapping[thing.name])
			things.sort()
			c += "".join(things)
		return c

	def nextStates(self):
		#if (self.steps > 2):
		#	return []

		destfloors = []
		if self.e < 3:
			# elevator can go up
			destfloors.append(self.e + 1)
		if self.e > 0:
			# elevator can go down
			destfloors.append(self.e - 1)

		cargo = list(combinations(self.floor[self.e], 1))
		cargo.extend(list(combinations(self.floor[self.e], 2)))

		children = []
		
		for d in destfloors:
			# we can move any combo of one or two things from our current floor
			for c in cargo:
				# moving c to floor d
				cf = []
				for f in range(0,4):
					if f == self.e: # remove from e
						cf.append(set([i for i in self.floor[f] if i not in c]))
					elif f == d: # deposit in d
						cf.append(self.floor[f] | set([i for i in self.floor[self.e] if i in c]))
					else: # shallow copy
						cf.append(self.floor[f])

				newstate = State(self.steps + 1, d, cf)
				cksum = newstate.checksum()

				if cksum not in checksums and isFloorSafe(cf):
					children.append(newstate)
					checksums.add(cksum)

		return children


#inputFloor = [
#	[Thing("M","hydrogen"), Thing("M","lithium")],
#	[Thing("G","hydrogen")], 
#	[Thing("G","lithium")],
#	[]
#]


inputFloor = [
	set([Thing("G","polonium"),Thing("G","thulium"),Thing("G","promethium"),Thing("G","ruthenium"),Thing("G","cobalt"),Thing("M","thulium"),Thing("M","ruthenium"),Thing("M","cobalt"),
		Thing("G","elerium"),Thing("G","dilithium"),Thing("M","elerium"),Thing("M","dilithium")]),
	set([Thing("M","polonium"),Thing("M","promethium")]),
	set(),
	set()
]

init = State(0, 0, inputFloor)
stateStack = deque([init])

print(init.checksum())


processed = 0

while len(stateStack) > 0:
	state = stateStack.popleft()
	processed += 1
	if (processed % 100 == 0):
		print("Depth " + str(state.steps) + ", Queue length: " + str(len(stateStack)) + ", processed: " + str(processed))
	if (state.isFinished()):
		print("Complete! steps: " + str(state.steps) + " - processed: " + str(processed))
		break
	ns = state.nextStates()
	stateStack.extend(ns)

