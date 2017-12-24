import math

def isComposite(b):
	for d in range(2,b):
		if b % d == 0:
			return True
	return False

h = 0

for b in range(109300,109300 + 17000 + 1,17):
	print "testing " + str(b)
	if isComposite(b):
		h += 1
		print str(b) + " composite"
	else:
		print str(b) + " prime"

print "final count: " + str(h)
