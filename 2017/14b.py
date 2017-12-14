from collections import deque

#input = "flqrgnkx"
input = 'stpzcrnm'

def knothash(input):
	print ("hashing " + input + "...")

	input = [ord(c) for c in input]

	# add standard suffix
	input += [17,31,73,47,23]

	list = range(0, 256)
	index = 0
	skip = 0

	def reverse(length):
		sublist = []
		for i in range(index, index + length):
			sublist.append(list[i % len(list)])
		
		sublist.reverse()

		for i in range(index, index + length):
			list[i % len(list)] = sublist[i - index]

	# run 64 passes of the algorithm	
	for i in range(0,64):
		for val in input:
			reverse(val)
			index += val + skip
			skip += 1

	# list is now the sparse hash

	def xorblock(block):
		return reduce(lambda a,b: a ^ b, block)

	# turn the sparse hash into a dense hash, array of binary
	hashval = ""
	for i in range(0,16):
		block = xorblock(list[i*16 : (i+1)*16])
		hashval += format(block, '08b')

	return hashval


rows = [knothash(input + "-" + str(r)) for r in range(0, 128)]
print "finding connected components..."

rows = [list(r) for r in rows] # turn it into a 2d array

def lookup(x,y):
	if x < 0 or x > 127 or y < 0 or y > 127: 
		return None
	return rows[x][y]

def next1():
	for y in range(0, 128):
		for x in range(0, 128):
			if lookup(x,y) == '1':
				return (x,y)

def adjacent1s(x,y):
	neighbors = [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
	return filter(lambda c: lookup(*c) == '1', neighbors)

def clearValue(x,y):
	rows[x][y] = ' ' # we've already seen this one

start = next1()

count = 0

while start != None:
	# find the first and flood fill until we run out
	q = deque([start])
	count += 1

	while q: 
		n = q.popleft()

		clearValue(*n)

		q.extend(adjacent1s(*n))

	start = next1()

print ("found " + str(count) + " ccs")



