discs = [] # (positions, start)

input = []
with open("Day15.txt") as f:
	input = f.readlines()

for line in input:
	words = line.strip().split(' ')
	discs.append((int(words[3]), int(words[11][:-1])))

def isValid(t):
	rval = True
	for i in range(0, len(discs)):
		#print(str(i) + ": " + str((discs[i][1] + t + 1) % discs[i][0]))
		if ((discs[i][1] + t + 1 + i) % discs[i][0]) != 0:
			#print("Fails on " + str(i) + ": (" + str(discs[i][1]) + " + " + str(t) + ") % " + str(discs[i][0]) + " == " + str((discs[i][1] + t + 1) % discs[i][0]))
			rval = False	
	return rval

t = 0
while not isValid(t) and t < 500000:
	#if t % 1000 == 0:
	print(str(t) + " invalid...")
	t += 1

print(str(t) + " valid!")
