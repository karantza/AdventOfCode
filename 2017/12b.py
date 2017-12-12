import re

input = open('12.txt', 'r').readlines()

parse = re.compile(r'(\d+) <-> (.*)')

nodes = {}
for n in input:
	m = parse.match(n)
	idx = int(m.group(1))
	children = [int(x) for x in m.group(2).split(',')]
	nodes[idx] = children


def components(start):
	# find items connected to nodes[start]
	seen = set()
	q = [start]
	while q:
		n = q.pop()
		seen.add(n)
		for c in nodes[n]:
			if c not in seen:
				q += [c]
	return seen

count = 0
seen = set([])
remainder = set(nodes.keys())
while remainder:
	count += 1
	cc = components(list(remainder)[0])
	seen |= cc
	remainder = remainder - cc
	print("Found " + str(count) + " ccs, remaining nodes: " + str(len(remainder)))

print count