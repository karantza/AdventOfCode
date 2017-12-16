import re
import time
from string import maketrans

input = open('16.txt', 'r').read()

input = input.split(',') 

original = 'abcdefghijklmnop'

def oneDance():
	indexLine = list(original)
	partnerLine = list(original)

	regexes = {
		's': re.compile(r's(\d+)'),
		'x': re.compile(r'x(\d+)/(\d+)'),
		'p': re.compile(r'p(\w)/(\w)') 
	}

	def swap(s):
		s = int(s)
		indexLine[:] = indexLine[-s:] + indexLine[:-s]

	def exchange(a,b):
		a = int(a)
		b = int(b)
		indexLine[a], indexLine[b] = indexLine[b], indexLine[a]

	def partner(a,b):
		a = partnerLine.index(a)
		b = partnerLine.index(b)
		partnerLine[a], partnerLine[b] = partnerLine[b], partnerLine[a]


	execute = {
		's': swap,
		'x': exchange,
		'p': partner
	}

	for instruction in input:
		ins = instruction[0]
		parse = regexes[ins].match(instruction)
		
		execute[ins](*parse.groups())

	partnerTrans = maketrans(original, ''.join(partnerLine))
	return ( [ord(x)-ord('a') for x in indexLine], partnerTrans)


# this boils the dance down to two matrices representing index swaps and value swaps
matrices = oneDance()


line = original;

sequence = []

while line not in sequence:
	print line
	sequence.append(line)
	line = ''.join([line[x] for x in matrices[0]])
	line = line.translate(matrices[1])

cycle = len(sequence)

print ("cycle length: " + str(cycle))
rem = 1000000000 % cycle
print ("remainder index: " + str(rem))
print sequence[rem]

