import re

input = open('16.txt', 'r').read()

input = input.split(',') 

print '\n'.join(input)

global line
line = list(map(chr, range(ord('a'), ord('p')+1)))

regexes = {
	's': re.compile(r's(\d+)'),
	'x': re.compile(r'x(\d+)/(\d+)'),
	'p': re.compile(r'p(\w)/(\w)') 
}

def swap(s):
	s = int(s)
	global line
	line = line[-s:] + line[:-s]

def exchange(a,b):
	a = int(a)
	b = int(b)
	global line
	line[a], line[b] = line[b], line[a]

def partner(a,b):
	global line
	exchange(line.index(a), line.index(b))

execute = {
	's': swap,
	'x': exchange,
	'p': partner
}

for instruction in input:
	ins = instruction[0]
	parse = regexes[ins].match(instruction)
	
	execute[ins](*parse.groups())

print ''.join(line)