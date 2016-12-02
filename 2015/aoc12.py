import json

input = open('aoc12.txt','r').read()

inputobj = json.loads(input)

def nored(x):
	if type(x) == int:
		return x
	if type(x) == list:
		return sum(nored(x) for x in x)
	if type(x) == dict:
		if 'red' in x.values():
			return 0
		else:
			return sum(nored(x) for x in x.values())
	return 0

print nored(inputobj)