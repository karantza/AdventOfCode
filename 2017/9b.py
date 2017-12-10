import re

input = open('9.txt', 'r').read()

def evaluate(input): 
	# preprocess the groups by applying some operations

	# remove !_
	input = re.sub("\!.", "", input)

	# find garbage
	clean = ""
	garbage = False
	garbageCount = 0
	for i in range(0, len(input)):
		if not garbage:
			if input[i] == '<':
				garbage = True
			else:
				clean += input[i]
		else:
			if input[i] == '>':
				garbage = False
			else:
				garbageCount += 1
				
	return garbageCount

print evaluate(input)