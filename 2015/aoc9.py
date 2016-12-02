
import re

cities = set()
routes = {}

f = open('aoc9.txt', 'r')
for line in f:
	m = re.match(r'(\w+) to (\w+) = (\d+)', line)
	a = m.group(1)
	b = m.group(2)
	dist = m.group(3)
	cities.add(a)
	cities.add(b)
	if a not in routes:
		routes[a] = {}
	routes[a][b] = int(dist)

	if b not in routes:
		routes[b] = {}
	routes[b][a] = int(dist)

mindist = 0#float("inf")
minroute = []

def goTo(city, visited, dist):
	visited = list(visited) # copy
	visited.append(city)

	if set(visited) == cities:
		print("dist: " + str(dist))
		global mindist
		global minroute

		if dist > mindist:
			mindist = dist
			minroute = visited
		return

	for neighbor in routes[city]:
		if neighbor not in visited:
			goTo(neighbor, visited, dist + routes[city][neighbor])

for city in cities:
	goTo(city, [], 0)
print(mindist, minroute)