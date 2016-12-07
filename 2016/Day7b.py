import re
from functools import partial

def ABAs(string):
	ABAs = []
	a = ''
	b = ''
	for i in range(0,len(string)-2):
		a = string[i]
		b = string[i+1]
		if a != b and (string[i+2] == a):
			ABAs.append(string[i:i+3])
	return ABAs

def containsBAB(string, aba):
	bab = aba[1] + aba[0] + aba[1]
	return bab in string

valid = []

with open("Day7.txt") as input:

	for ip in input:
		#remove square bracket sequences
		outside = re.sub(r'\[[a-z]*\]','____', ip)
		inside = re.findall(r'\[[a-z]*\]', ip)

		abas = ABAs(outside)

		for aba in abas: 
			f = partial(containsBAB,aba=aba)
			if any(map(f,inside)):
				valid.append(ip)
				break


print "\n".join(valid)
print len(valid)