
input = open('11.txt', 'r').read()
# skew mapping:
# NW N --
# SW O NE
# -- S SE

def add(a, b):
	return tuple([x + y for x, y in zip(a, b)])

direction = {
	'n': (0, -1),
	's': (0, +1),
	'ne': (+1, 0),
	'se': (+1, +1),
	'nw': (-1, -1),
	'sw': (-1, 0),
}


def solve(input):

	input = input.split(',')

	location = (0,0)

	# find the shortest route to this point

	def nextDir(tgt, pos):
		if (tgt[0] > pos[0]): # must go east
			if (tgt[1] > pos[1]): # must go south
				return 'se' # diagonal
			else:
				return 'ne'
		elif (tgt[0] < pos[0]): # must go west
			if (tgt[1] < pos[1]): # must go north
				return 'nw' # diagonal
			else:
				return 'sw'
		else: # n or s only
			if (tgt[1] < pos[1]): # must go north
				return 'n'
			else:
				return 's'

	def dist(loc):
		trace = (0,0)
		count = 0

		while trace != loc:
			trace = add(trace, direction[nextDir(loc, trace)])
			count += 1
		return count


	maxD = 0;

	# move to our destination
	for dir in input:
		location = add(location, direction[dir])
		D = dist(location)
		if D > maxD:
			maxD = D

	return maxD



print solve(input)