input = [("Vixen",19,7,124), 
("Rudolph",3,15,28), 
("Donner",19,9,164), 
("Blitzen",19,9,158), 
("Comet",13,7,82), 
("Cupid",25,6,145), 
("Dasher",14,3,38), 
("Dancer",3,16,37), 
("Prancer",25,6,143)]

race = 2503

names = map(lambda x: x[0], input)

def deerflying(x, deer):
	deercycle = deer[2]+deer[3]
	x = x % deercycle
	return x < deer[2]

distance = dict(zip(names, [0]*len(names)))
points = dict(zip(names, [0]*len(names)))

for x in range(0, race):
	for deer in input:
		if (deerflying(x, deer)):
			distance[deer[0]] += deer[1]

	m = max(distance.values())
	for deer in input:
		if (distance[deer[0]] == m):
			points[deer[0]] += 1
			print(deer[0],m,points[deer[0]])


print(points)
print(distance)
print(max(points.values()))

