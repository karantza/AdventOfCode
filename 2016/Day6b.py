
with open('Day6.txt', 'r') as file:
	input = file.read().splitlines()

	strlen = max([len(x) for x in input])

	message = ""
	for i in range(0, strlen):
		char = [x[i] for x in input]
		message += min(set(char), key=char.count)

	print message