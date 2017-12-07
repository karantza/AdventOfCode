import re
from collections import Counter

class Node:
	name = ""
	weight = 0
	towerWeight = 0
	children = []
	parent = None
	balanced = True

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return self.name + " (" + str(self.towerWeight) + "), \t" + str(self.balanced)


def loadNodeGraph():
	nodesByName = {}

	with open('7.txt', 'r') as file:
	    total = 0
	    for nodestr in file:
			m = re.match('([a-z]*) \((\d*)\)( -> )?([a-z, ]+)?', nodestr)
			
			name = m.group(1)
			weight = int(m.group(2))
			children = m.group(4)

			if children:
				children = children.split(', ')
			else:
				children = []

			n = Node()
			n.name = name
			n.weight = weight
			n.children = children # strings for now

			nodesByName[name] = n

	# now go and replace the string names with proper links
	for n in nodesByName.values():
		newChildren = []
		for c in n.children:
			newChildren.append(nodesByName[c])
			nodesByName[c].parent = n
		n.children = newChildren

	return nodesByName



# find the root
graph = loadNodeGraph().values()
root = graph[0]
while root.parent:
	root = root.parent

# go through the tree to find the weights
def calcTowerWeight(n):
	n.towerWeight = sum([calcTowerWeight(c) for c in n.children]) + n.weight
	return n.towerWeight
calcTowerWeight(root)

# which nodes are not balanced?
for n in graph:
	if len(n.children) == 0:
		n.balanced = True
	else:
		ctw = [c.towerWeight for c in n.children]
		n.balanced = all(ctw[0] == x for x in ctw)

n = root
while True:
	# find the unbalanced child
	ubc = [c for c in n.children if not c.balanced]
	if len(ubc) == 0:
		break # all our children are balanced, but we are not! a child's weight is wrong
	else:
		n = ubc[0]

weights = Counter([c.towerWeight for c in n.children])
expected = weights.most_common(1)[0][0]

for c in n.children:
	if c.towerWeight == expected:
		continue
	delta = expected - c.towerWeight
	print("node " + c.name + " adjusted by " + str(delta) + " so its weight is " + str(c.weight + delta))