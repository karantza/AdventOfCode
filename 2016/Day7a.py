import re

def containsABBA(string):
	a = ''
	b = ''
	for i in range(0,len(string)-3):
		a = string[i]
		b = string[i+1]
		if a != b and (string[i+2] == b) and (string[i+3] == a):
			return True
	return False

valid = []

with open("Day7.txt") as input:
	for ip in input:
		#remove square bracket sequences
		outside = re.sub(r'\[[a-z]*\]','____', ip)
		inside = re.findall(r'\[[a-z]*\]', ip)

		if containsABBA(outside) and not any(map(containsABBA,inside)):
			valid.append(ip)


print "\n".join(valid)
print len(valid)