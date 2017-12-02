input = []
with open("Day20.txt") as f:
	input = [tuple([int(y) for y in x.strip().split('-')]) for x in f.readlines()]

blocked = sorted(input, key=lambda x: x[0])

print('\n'.join([str(x) for x in blocked]))

top = 0

for i in blocked:
	if (i[0] <= top): # we overlap
		top = max(top, i[1]+1)
		print("Increasing top to " + str(top))

print("First unblocked: " + str(top))