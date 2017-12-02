import re

class Node:
	def __init__(self, coord,size,used,avail):
		self.coord = coord
		self.size = size
		self.used = used
		self.avail = avail

	def __repr__(self):
		return str(self.coord) + "\t" + str(self.size) + "\t" + str(self.used) + "\t" + str(self.avail)

#/dev/grid/node-x0-y0     94T   65T    29T   69%

df = re.compile('/dev/grid/node-x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%')
input = []
with open("Day22.txt") as f:
	for x in f.readlines():
		m = df.match(x)
		coord = (int(m.group(1)),int(m.group(2)))
		input.append(Node(coord, int(m.group(3)), int(m.group(4)), int(m.group(5))))

viable = []
#Node A is not empty (its Used is not zero).
#Nodes A and B are not the same node.
#The data on node A (its Used) would fit on node B (its Avail).

for a in input:
	for b in input:
		if a.used > 0 and a != b and a.used <= b.avail:
			print("a.used = " + str(a.used) + " and b.avail = " + str(b.coord))
			viable.append((a,b))

print(str(len(viable)) + " viable pairs")
