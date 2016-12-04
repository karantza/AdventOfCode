import re
import string

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

def decrypt(name, sector):
	shift = sector % 26;
	alphabet = string.ascii_lowercase
	decoder = alphabet[shift:] + alphabet[:shift]
	table = string.maketrans(alphabet, decoder)
	return name.translate(table)


with open('Day4.txt', 'r') as file:

    for roomstr in file:
		m = re.match('([a-z-]*)-(\d*)\[([a-z]*)\]', roomstr)
		
		name = ''.join(m.group(1).split('-'))
		namestr = m.group(1)
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
			realname = decrypt(namestr, sector)
			if realname == "northpole-object-storage":
				print(sector)

