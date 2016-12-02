import sys
lights = [] 

stuck = True

f = open('aoc18.txt', 'r')
y = 0
for line in f:
	x = 0
	row = []
	for c in line:
		if c == '.':
			row.append(False)
			x += 1
		if c == '#':
			row.append(True)
			x += 1
	lights.append(row)
	y += 1

def display():
	for row in lights:
		for x in row:
			symbol = '#' if x else '.'
			sys.stdout.write(symbol)
		print
	print

def lightAt(x,y):
	if (x < 0 or x >= len(lights[0])):
		return False
	if (y < 0 or y >= len(lights)):
		return False
	return lights[x][y]

def step():
	global lights
	newLights = [['?' for x in range(0,len(lights[0]))] for x in range(0, len(lights))]

	for y in range(0, len(lights)):
		for x in range(0, len(lights[y])):
			neighbors = [
				lightAt(x-1, y-1),
				lightAt(x  , y-1),
				lightAt(x+1, y-1),
				lightAt(x-1, y),
				lightAt(x+1, y),
				lightAt(x-1, y+1),
				lightAt(x  , y+1),
				lightAt(x+1, y+1)]
			numNeighbors = len(filter(lambda x: x, neighbors))

			newLights[x][y] = (lights[x][y] and (numNeighbors == 2 or numNeighbors == 3)) or (not lights[x][y] and numNeighbors == 3)

	newLights[0][0] = True
	newLights[0][len(lights)-1] = True
	newLights[len(lights[0])-1][0] = True
	newLights[len(lights[0])-1][len(lights)-1] = True


	lights = newLights

display()
for i in range(0, 100):
	step()
	display()

print(sum(map(sum,lights)))

