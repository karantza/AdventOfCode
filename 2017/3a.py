from math import *

input = 265149

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
		return (x,y)

	if (i <= c): # top side
		x = -n  + (c - i)
		y = -n
		return (x,y)

	if (i <= d): # left side
		x = -n
		y = n - (d - i)
		return (x,y)

	if (i <= e): # top side
		x = n - (e - i)
		y = n
		return (x,y)

def distance(a):
	return int(abs(a[0] + a[1]))

print distance(coordinate(input))