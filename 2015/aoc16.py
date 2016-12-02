import re

target = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1,
}

sues = []

fmt = re.compile(r'Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

def compare(field, value):
	if field == "cats" or field == "trees":
		return value > target[field]
	if field == "pomeranians" or field == "goldfish":
		return value < target[field]
	return value == target[field]

f = open('aoc16.txt', 'r')
for line in f:
	m = re.match(fmt, line)

	sue = {
		m.group(1): m.group(2),
		m.group(3): m.group(4),
		m.group(5): m.group(6)
		}
	sues.append(sue)

	if compare(m.group(1), int(m.group(2))) and compare(m.group(3), int(m.group(4))) and compare(m.group(5), int(m.group(6))):
		print(m.group(0))
