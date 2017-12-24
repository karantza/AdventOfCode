from copy import deepcopy

#input = ["../.# => ##./#../...",".#./..#/### => #..#/..../..../#..#"]
input = [x.strip() for x in open('21.txt', 'r').readlines()]
print input

global rules
rules = {}
for x in input:
	ps = x.split(' => ')
	rules[ps[0]] = ps[1]

grid = [list(".#."),list("..#"),list("###")]
#grid = [list("#..#"),list("...."),list("...."),list("#..#")]

def printGrid(g):
	print( '\n'.join([''.join(l) for l in g]))

def compactGrid(g):
	return ( '/'.join([''.join(l) for l in g]))


def getSubgrid(x,y,size):
	return [ line[x:x+size] for line in grid[y:y+size] ]

def flip(subgrid):
	return reversed(subgrid)

def rotate(subgrid):
	size = len(subgrid)

	newgrid = deepcopy(subgrid) # copy
	
	for x in range(0, size):
		for y in range(0, size):
			newgrid[y][x] = subgrid[x][size - y - 1]
	
	return newgrid

def matchesRule(subgrid):
	global rules
	gridString = compactGrid(subgrid)
	if gridString in rules:
		return rules[gridString]

def findMatchingRule(subgrid):

	options = [
		subgrid,
		rotate(subgrid),
		rotate(rotate(subgrid)),
		rotate(rotate(rotate(subgrid))),

		flip(subgrid),
		flip(rotate(subgrid)),
		flip(rotate(rotate(subgrid))),
		flip(rotate(rotate(rotate(subgrid)))),
	]

	for o in options:
		rule = matchesRule(o)
		if rule:
			return rule
	return

for iteration in range(0, 18):

	size = len(grid)
	if size % 2 == 0:
		subgrids = size / 2
		subgridsize = 2
	elif size % 3 == 0:
		subgrids = size / 3
		subgridsize = 3

	print("iteration: " + str(iteration) + " grid size: " + str(size) + " subgrids: " + str(subgrids) + " of size " + str(subgridsize))

	sgs = [[ getSubgrid(x*subgridsize,y*subgridsize,subgridsize) for x in range(0, subgrids)] for y in range(0, subgrids)]

	replacements = [ [ '?' for x in range(0,subgrids)] for x in range(0,subgrids)]

	newgridsize = subgrids * (subgridsize + 1)
	newgrid = [ [ ' ' for x in range(0,newgridsize)] for x in range(0,newgridsize)]

	for x in range(0, subgrids):
		for y in range(0,subgrids):
			replacements[y][x] = findMatchingRule(sgs[y][x])

	for x in range(0, newgridsize):
		for y in range(0,newgridsize):
			replacementx = int(x / (subgridsize + 1))
			replacementy = int(y / (subgridsize + 1))
			replacement = replacements[replacementy][replacementx].split('/')
			newgrid[y][x] = replacement[y % (subgridsize + 1)][x % (subgridsize + 1)]
	
	grid = newgrid

	print ("iteration: " + str(iteration) + ": active pixel count = " + str(sum([line.count('#') for line in grid])))
	
