import string

#input = """     |          
#     |  +--+    
#     A  |  C    
# F---|----E|--+ 
#     |  |  |  D 
#     +B-+  +--+ """.split('\n')

input = open('19.txt', 'r').readlines()

def at(c):
	return input[c.y][c.x]
def at(x,y):
	return input[y][x]

class Coord:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.val = at(x,y)

def step(start, dir):
	# we only change direction if we're on a +
	if start.val == '+':
		dirs = [(-1,0), (1,0), (0, -1), (0,1)]
		for d in dirs:
			if d[0] == -dir[0] and d[1] == -dir[1]:
				continue
			test = Coord(start.x + d[0], start.y + d[1])
			if test.val != ' ':
				# we should go here
				return (test, d)

	# not on a +, we keep going
	next = Coord(start.x + dir[0], start.y + dir[1])
	return (next, dir)

step
dir = (0, 1)
position = Coord(input[0].find('|'), 0)

sequence = []

while position.val != ' ':
	position, dir = step(position, dir)
	#print (position.x, position.y, position.val, dir)
	if position.val in string.ascii_uppercase:
		sequence.append(position.val)

print ''.join(sequence)
