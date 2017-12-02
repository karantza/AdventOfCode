input = 3014603
#input = 5

elves = range(1,input+1);

def next(i):
	j = (i + 1) % input;
	while elves[j] == None:
		j = (j + 1) % input;
	return j

i = 0;
elfcount = input

while elfcount > 1:
	# index i removes i + 1
	i = i % input
	j = next(i);
	
	#print(str(i) + ": " + str(elves[i]) + " removes " + str(elves[j]))
	elves[j] = None
	elfcount -= 1
	i = next(i)

print("Remaining: " + str(elves[i]))