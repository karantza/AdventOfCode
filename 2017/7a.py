import re

class Node:
	name = ""
	weight = 0
	children = []
	parent = None

	def __str__(self):
		return self.__repr__()

	def __repr__(self):
		return self.name + " (" + str(self.weight) + ")\n"


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

print root
