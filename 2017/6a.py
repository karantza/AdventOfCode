input = [int(x) for x in open('6.txt', 'r').read().split("\t")]

known = set([])

banks = len(input); 
current = input
cycles = 0

while str(current) not in known:
	# remember this one
	known.add(str(current))

	# find biggest bank
	biggest = 0;
	for i in range(0, banks):
		if (current[i] > current[biggest]): # < means ties go to the first one
			biggest = i

	# redistribute
	pile = current[biggest]
	current[biggest] = 0
	insert = biggest

	while pile > 0:
		insert = (insert + 1) % banks # move to the next
		pile = pile - 1 # take one off the pile
		current[insert] = current[insert] + 1 # and add to the bank

	# pile depleted, cycle done
	cycles = cycles + 1
	print("cycle " + str(cycles) + ": " + str(current))

print ("took " + str(cycles) + " cycles")