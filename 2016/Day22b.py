import re
import Queue as Q
from copy import copy, deepcopy

class Node:
	def __init__(self, coord,size,used,avail):
		self.coord = coord
		self.size = size
		self.used = used
		self.avail = avail
		if used > 100:
			self.symbol = "#"
		elif used == 0:
			self.symbol = "_"
		else:
			self.symbol = "."

	def __repr__(self):
		return self.symbol

class State:
	def __init__(self, grid):
		self.grid = grid
		for y in range(0,len(self.grid)):
			for x in range(0, len(self.grid[y])):
				if self.grid[y][x] == '_':
					self.emptySpace = (x,y)



	def children(self):
		children = []

		for d in [(-1,0),(1,0),(0,-1),(0,1)]:

			newempty = (self.emptySpace[0] + d[0], self.emptySpace[1] + d[1])
			
			if newempty[0] < 0 or newempty[0] > maxX or newempty[1] < 0 or newempty[1] >= len(self.grid):
			#	print("cannot swap out of bounds, aborting")
				continue
			
			toSwap = self.grid[newempty[1]][newempty[0]]
			
			if toSwap == '#':
			#	print("would swap with wall, aborting")
				continue

			newgrid = deepcopy(self.grid)
			newgrid[newempty[1]][newempty[0]] = '_'
			newgrid[self.emptySpace[1]][self.emptySpace[0]] = toSwap
			children.append(State(newgrid))
		return children

	def key(self):
		s = ""
		for y in self.grid:
			row = ""
			for x in y:
				row += x
			s += row
		return s

	def __repr__(self):
		s = ""
		for y in self.grid:
			row = ""
			for x in y:
				row += x
			s += row + "\n"
		return s

#/dev/grid/node-x0-y0     94T   65T    29T   69%

maxX = 0
maxY = 0
nodes = {}

df = re.compile('/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%')
with open("Day22.txt") as f:
	for x in f.readlines():
		m = df.match(x)
		coord = (int(m.group(1)),int(m.group(2)))
		n = Node(coord, int(m.group(3)), int(m.group(4)), int(m.group(5)))
		maxX = max(maxX, coord[0])
		maxY = max(maxY, coord[1])
		nodes[coord] = n

nodes[(0,0)].symbol = "D"
nodes[(maxX,0)].symbol = "S"
nodes[(33,0)].symbol = "_"

initialGrid = []
for y in range(0, 2):
	row = []
	for x in range(0, maxX+1):
		row.append(str(nodes[(x,y)]))
	initialGrid.append(row)

initialState = State(initialGrid)
print(initialState)

q = Q.Queue()
q.put(initialState)

visited = { initialState.key() : 34 }

while not q.empty():
	state = q.get()
	d = visited[state.key()]

	if (state.grid[0][0] == 'S'):
		print("Found path: depth " + str(d))
		break

	newdepth = d + 1
	#print("Searching at depth " + str(newdepth) + ".. " + str(state))
	print(newdepth)
	ns = state.children()
	for n in ns:
		#print("Checking state...")
		nstr = n.key()
		if nstr not in visited or visited[nstr] > newdepth:
			visited[nstr] = newdepth
			q.put(n)

