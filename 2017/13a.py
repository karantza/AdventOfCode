import re

input = [x.split(': ') for x in open('13.txt', 'r').readlines()]
wall = {}
for x in input:
	wall[int(x[0])] = int(x[1])


# the sensor has a cycle of 2(d-1)
# so a collision at time t happens if
# t % 2(d-1) = 0

def caught(t):
	d = wall[t]
	s = t % (2*(d-1))
	return s == 0

severity = 0
for t in wall.keys():
	if caught(t):
		severity += t * wall[t]

print severity