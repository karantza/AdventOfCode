import hashlib
import Queue as Q


input = 'bwnlcvfs'

def md5(x):
	return hashlib.md5(x).hexdigest()

def validPos(pos):
	return not (pos[0] < 0 or pos[0] > 3 or pos[1] < 0 or pos[1] > 3)

def coordFor(i, pos):
	if i == 0:
		return ('U', (pos[0],pos[1]-1))
	if i == 1:
		return ('D', (pos[0],pos[1]+1))
	if i == 2:
		return ('L', (pos[0]-1,pos[1]))
	if i == 3:
		return ('R', (pos[0]+1,pos[1]))

def options(state):
	route = state[0]
	pos = state[1]

	hash = md5(input + route)
	options = []

	for i in range(0,4):
		c = coordFor(i, pos)
		print(str(i) + ": " + str(c))
		if hash[i] in "bcdef" and validPos(c[1]):
			options.append((route + c[0], c[1]))

	return options

q = Q.Queue()
q.put(('', (0,0)))

while not q.empty():
	c = q.get()
	if c[1] == (3,3):
		print("Found fastest route: " + str(c))
		break

	print("processing route... " + str(c))
	next = options(c)
	for i in next:
		q.put(i)



