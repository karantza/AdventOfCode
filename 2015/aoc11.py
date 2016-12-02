lookup = ['a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z']

def isvalid(p):
	valid = False
	for i in range(6):
		if p[i+1] == p[i]+1 and p[i+2] == p[i+1]+1:
			valid = True
			break
	if not valid:
		return False

	match1 = None
	for i in range(7):
		if p[i] == p[i+1]:
			match1 = p[i]
			break
	if match1 == None:
		return False

	match2 = None
	for i in range(7):
		if p[i] == p[i+1] and p[i] != match1:
			match2 = p[i]
			break
	if match2 == None:
		return False
	
	return True

def increment(p):
	i = 7
	p[i] += 1

	while p[i] >= len(lookup):
		p[i] = 0 
		p[i-1] += 1
		i -= 1

start = "hxbxwxba"
startl = []
for c in start:
	startl.append(lookup.index(c))

while not isvalid(startl):
	increment(startl)

increment(startl)


while not isvalid(startl):
	increment(startl)


print(startl)

nd = ""
for x in startl:
	nd += lookup[x]

print nd

