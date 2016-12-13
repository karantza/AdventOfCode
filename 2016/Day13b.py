import Queue as Q

input = 1352
dest = (31,39)

class Coord(object):
	def __init__(self, c):
		self.x = c[0]
		self.y = c[1]
		self.c = c
		self.dist = abs(self.x - dest[0]) + abs(self.y - dest[1])

 	def __cmp__(self, other):
 		return self.dist.__cmp__(other.dist)

visited = {}

def isWall(coord):
	x = coord[0]
	y = coord[1]
	i = x*x + 3*x + 2*x*y + y + y*y + input
	c = bin(i).count('1')
	return c % 2 == 1

def icon(c):
	if isWall(c):
		return "#"
	elif c == dest:
		return "X"
	elif c in visited:
		return str(visited[c]%10)
	else:
		return "."

def neighbors(c):
	r = []
	pr = [(c[0]-1, c[1]),
		(c[0]+1, c[1]),
		(c[0], c[1]-1),
		(c[0], c[1]+1)]
	for pc in pr:
		if pc[0] < 0 or pc[1] < 0:
			continue
		if not isWall(pc):
			r.append(pc)
	return r

def display(w,h):
	for y in range(0,h):
		print "".join([icon((x,y)) for x in range(0,w)])
			
queue = Q.Queue()

queue.put(Coord((1,1)))
visited[(1,1)] = 0

while True:
	c = queue.get()
	
	print("")
	depth = visited[c.c] + 1
	if depth == 51:
		break

	ns = neighbors(c.c)
	for n in ns:
		if n not in visited:
			visited[n] = depth
			queue.put(Coord(n))


	v = visited.keys()
	maxx = max([i[0] for i in v])
	maxy = max([i[1] for i in v])

	display( maxx+2, maxy+2 )

print ("Visited a total of " + str(len(visited)))