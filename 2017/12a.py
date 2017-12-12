import re

input = open('12.txt', 'r').readlines()

parse = re.compile(r'(\d+) <-> (.*)')

nodes = {}
for n in input:
	m = parse.match(n)
	idx = int(m.group(1))
	children = [int(x) for x in m.group(2).split(',')]
	nodes[idx] = children


# find items connected to nodes[0]
seen = set()
q = [0]
while q:
	n = q.pop()
	seen.add(n)
	for c in nodes[n]:
		if c not in seen:
			q += [c]

print len(seen)