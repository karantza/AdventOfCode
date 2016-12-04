import re

def compare(a, b):
	if a[1] < b[1]:
		return 1
	elif a[1] > b[1]:
		return -1
	else:
		if a[0] > b[0]:
			return 1
		else:
		 	return -1


with open('Day4.txt', 'r') as file:
    total = 0
    for roomstr in file:
		m = re.match('([a-z-]*)-(\d*)\[([a-z]*)\]', roomstr)
		
		name = ''.join(m.group(1).split('-'))
		sector = int(m.group(2))
		checksum = m.group(3)

		# compute the correct checksum
		freq = {}
		for c in set(name):
			freq[c] = name.count(c)

		freq = freq.items() # convert to list of tuples
		freq.sort(cmp=compare)
		topfive = freq[:5]

		newchecksum = ''.join([x[0] for x in topfive])

		if newchecksum == checksum:
			total += sector

    print (total)
