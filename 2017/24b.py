
#input = ["0/2","2/2","2/3","3/4","3/5","0/1","10/1","9/10"]
input = open('24.txt', 'r').readlines()

components = [[int(i) for i in x.split('/')] for x in input]

ports = {}

def addTo(dict, k, v):
	if k in dict:
		dict[k].add(v)
	else:
		dict[k] = set([v])

for i,c in enumerate(components):
	addTo(ports, c[0], i)
	addTo(ports, c[1], i)
	
# routes are arrays of tuples; an index, and a bool indicating if it's flipped.
# for example, [(0, False), (3, False), (2, True)]


def findBridgesFrom(port, bridge, used):

	bridges = []

	# find unused nodes that have port available
	nextidxs = [i for i in ports[port] if i not in used]

	for ni in nextidxs:
		flipped = components[ni][0] != port
		newbridge = bridge + [(ni, flipped)]
		bridges.append(newbridge)
		newused = used + [ni]
		nextport = components[ni][0] if flipped else components[ni][1]
		bridges += findBridgesFrom(nextport, newbridge, newused)

	return bridges


def strengthOfBridge(bridge):
	strength = 0
	for i in bridge:
		component = components[i[0]]
		strength += component[0]
		strength += component[1]
	return strength

bridges = findBridgesFrom(0, [], [])
maxBridgeLen = max([len(b) for b in bridges])

bridgesOfMaxLen = [b for b in bridges if len(b) == maxBridgeLen]

print max([strengthOfBridge(b) for b in bridgesOfMaxLen])
