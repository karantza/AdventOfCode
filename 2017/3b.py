from math import *
from collections import namedtuple

input = 265149

Coord = namedtuple("Coord", "x y")

#from part 1, find coordinate of index
def coordinate(i):
	# calculate ring
	n = floor((sqrt(i - 1) + 1) / 2) 
	# c . . b
	# .     .
	# .     a
	# d . . e
	# calculate the corner coordinates
	a = pow(2*n-1, 2) + 1
	b = a + 2*n - 1
	c = b + 2*n
	d = c + 2*n
	e = d + 2*n
	
	if (i <= b): # right side
		x = n
		y = -n + (b - i)
		return Coord(x,y)

	if (i <= c): # top side
		x = -n  + (c - i)
		y = -n
		return Coord(x,y)

	if (i <= d): # left side
		x = -n
		y = n - (d - i)
		return Coord(x,y)

	if (i <= e): # top side
		x = n - (e - i)
		y = n
		return Coord(x,y)

knownValues = {Coord(0,0) : 1}

i = 2 # index of entry

# return the sum of surrounding filled in entries
def surround(c):
	acc = 0
	for x in range(int(c.x - 1), int(c.x + 2)):
		for y in range(int(c.y - 1), int(c.y + 2)):
			if x == c.x and y == c.y:
				continue
			v = knownValues.get(Coord(x,y))
			if (v != None):
				acc += v
	return acc
			
# go through each index until we hit one larger than our value
value = 0;
while (value < input):
	c = coordinate(i)
	value = surround(c)
	knownValues[c] = value
	i = i + 1
	
print value
for y in range(-2, 3):
	print "\t".join([str(knownValues.get(Coord(x,y))) for x in range(-2, 3)])

