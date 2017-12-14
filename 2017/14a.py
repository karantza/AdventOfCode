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

print ("counting used values...")
used = sum([x.count('1') for x in rows])

print used