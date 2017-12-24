
import operator

total = 10000000

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
	if (burst % (total / 100)) == 0:
		print str(int(100 * burst / total)) + '%'

	if carrierPos in infected:
		thisValue = infected[carrierPos]
	else:
		thisValue = '.'

	if thisValue == '.':
		carrierDir = turnLeft(carrierDir)
		infected[carrierPos] = 'W'
	elif thisValue == 'W':
		infected[carrierPos] = '#'		
		infectCount += 1
	elif thisValue == '#':
		carrierDir = turnRight(carrierDir)
		infected[carrierPos] = 'F'
	elif thisValue == 'F':
		carrierDir = turnRight(carrierDir)
		carrierDir = turnRight(carrierDir)
		infected.pop(carrierPos, None)

	carrierPos = moveForward(carrierPos, carrierDir)

print infectCount