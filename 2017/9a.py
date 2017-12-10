import re

input = open('9.txt', 'r').read()

def evaluate(input): 
	# preprocess the groups by applying some operations

	# remove !_
	input = re.sub("\!.", "", input)

	# find garbage
	clean = ""
	garbage = False
	for i in range(0, len(input)):
		if not garbage:
			if input[i] == '<':
				garbage = True
			else:
				clean += input[i]
		else:
			if input[i] == '>':
				garbage = False

	# now count up the depth of blocks
	depth = 0
	score = 0
	for c in clean:
		if c == "{":
			depth += 1
			score += depth
		if c == "}":
			depth -= 1

	return score

print evaluate(input)