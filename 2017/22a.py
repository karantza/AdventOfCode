
import operator

total = 10000

infected = {}

#startingMap = ['..#','#..','...']
startingMap = open('22.txt','r').readlines()

startingCoord = int(len(startingMap) / 2)

for x in range(-startingCoord, startingCoord + 1):
	for y in range(-startingCoord, startingCoord + 1):
		if startingMap[y+startingCoord][x+startingCoord] == '#':
			infected[(x,y)] = '#' # starts infected

carrierPos = (0,0)
carrierDir = (0,-1)

def turnRight(dir):
	if dir == (0,1):
		return (-1,0)
	if dir == (0,-1):
		return (1,0)
	if dir == (1,0):
		return (0,1)
	if dir == (-1,0):
		return (0,-1)

def turnLeft(dir):
	if dir == (0,1):
		return (1,0)
	if dir == (0,-1):
		return (-1,0)
	if dir == (1,0):
		return (0,-1)
	if dir == (-1,0):
		return (0,1)

def moveForward(pos, dir):
	return tuple(map(operator.add, pos, dir))

infectCount = 0

for burst in range(0, total):
	if carrierPos in infected:
		carrierDir = turnRight(carrierDir)
		infected.pop(carrierPos, None)
	else:
		carrierDir = turnLeft(carrierDir)
		infected[carrierPos] = True
		infectCount += 1

	carrierPos = moveForward(carrierPos, carrierDir)

	print infectCount

def printGrid(grid):
	coords = grid.keys()
	xmin = 0
	ymin = 0
	xmax = 0
	ymax = 0
	for c in coords:
		xmin = min(xmin, c[0])
		xmax = max(xmax, c[0])
		ymin = min(ymin, c[1])
		ymax = max(ymax, c[1])

	for y in range(ymin-1, ymax+2):
		line = ''
		for x in range(xmin-1, xmax+2):
			if (x,y) in coords:
				line += '#'
			else:
				line += '.'
		print line


#printGrid(infected)


