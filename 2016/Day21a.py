import re

input = []
with open("Day21.txt") as f:
	input = [x.strip() for x in f.readlines()]

def swapPosition(m, x):
	a = int(m.group(1))
	b = int(m.group(2))
	x[a],x[b] = x[b],x[a]
	return x

def swapLetters(m, x):
	a = m.group(1)
	b = m.group(2)
	for i in range(0,len(x)):
		if x[i] == a:
			x[i] = b
		elif x[i] == b:
			x[i] = a
	return x

def rotateLeft(m,x):
	r = int(m.group(1))
	return x[r:] + x[:r]
	
def rotateRight(m,x):
	r = int(m.group(1))
	return x[-r:] + x[:-r]
	
def rotateLetter(m,x):
	a = m.group(1)
	i = x.index(a)
	r = (1 + i + (1 if i >= 4 else 0)) % len(x)
	return (x[-r:] + x[:-r])

def reverse(m,x):
	a = int(m.group(1))
	b = int(m.group(2))+1
	center = x[a:b]
	center.reverse()
	return (x[:a] + center + x[b:])

def move(m,x):
	a = int(m.group(1))
	b = int(m.group(2)) 
	v = x.pop(a)
	x.insert(b, v)
	return x

instructions = [(re.compile('swap position (\d+) with position (\d+)'), swapPosition),
				(re.compile('swap letter (\w) with letter (\w)'), swapLetters),
				(re.compile('rotate left (\d+) steps?'), rotateLeft),
				(re.compile('rotate right (\d+) steps?'), rotateRight),
				(re.compile('rotate based on position of letter (\w)'), rotateLetter),
				(re.compile('reverse positions (\d+) through (\d+)'), reverse),
				(re.compile('move position (\d+) to position (\d+)'), move)]

def executeInstruction(i, x):
	for rei in instructions:
		m = rei[0].match(i)
		if m:
			return rei[1](m,x) 
	print("Error, could not deal with instruction " + i)

value = list('abcdefgh')
print ("> " + ''.join(value))

for i in input:
	value = executeInstruction(i, value)
	print (i + " > " + ''.join(value))
