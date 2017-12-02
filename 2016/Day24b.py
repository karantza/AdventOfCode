import Queue as Q
import itertools

maxnumber = 7

rows = []
waypoints = {}

with open("Day24.txt") as f:
	rows = [x.strip() for x in f.readlines()]

for i in range(0,maxnumber+1):
	for y in range(0, len(rows)):
		x = rows[y].find(str(i))
		if x >= 0:
			waypoints[i] = (x, y)

print("Waypoints: " + str(waypoints))

def optionsFrom(c):
	# return an array of valid coordinates adjacent to c
	offset = [
		(c[0]-1,c[1]), 
		(c[0]+1,c[1]), 
		(c[0],c[1]-1), 
		(c[0],c[1]+1)
		] 
	
	rval = []
	for c in offset:
		#print("Checking " + str(c))
		if c[1] >= 0 and c[1] < len(rows) and c[0] >= 0 and c[0] < len(rows[c[1]]):
			#print ("is " + str(rows[c[1]][c[0]]))
			if rows[c[1]][c[0]] != '#':
				rval.append(c)
	return rval


pathCache = {}
def fromAtoB(a,b):
	
	if (a,b) in pathCache:
		return pathCache[(a,b)]

	visited = []

	# find fastest path from a to b
	q = Q.Queue()
	initialState = (a,0)
	q.put(initialState)
	while not q.empty():
		s = q.get()
		
		if s[0] in visited:
			continue
		visited.append(s[0])

		if s[0] == b:
			pathCache[(a,b)] = s[1]
			#print("in cache, " + str(s[1]))
			return s[1]
		else:
			c = optionsFrom(s[0])
			#print("looking around, " + str(c) + " options")
			[q.put((cs, s[1]+1)) for cs in c]
	# can't get theah from heah
	return 9999


# return steps it takes to visit all nodes in this order
def inThisOrder(order):
	route = 0
	for i in range(0,len(order)-1):
		leg = fromAtoB(order[i], order[i+1])
		print("Leg from " + str(order[i]) + " to " + str(order[i+1]) + ": " + str(leg))
		route += leg
	return route

def coordFromWaypoints(wps):
	return [waypoints[w] for w in wps]

routes = list(itertools.permutations(range(1,maxnumber+1)))
routes = [[0] + list(x) + [0] for x in routes]

minRoute = 9999
for r in routes:
	d = inThisOrder(coordFromWaypoints(r))
	print(str(r) + " takes " + str(d))
	if d < minRoute:
		minRoute = d

print("Path cache: " + str(pathCache))
print("Fastest route: " + str(minRoute))
