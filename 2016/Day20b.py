input = []
with open("Day20.txt") as f:
	input = [tuple([int(y) for y in x.strip().split('-')]) for x in f.readlines()]

blocked = sorted(input, key=lambda x: x[0])

print('\n'.join([str(x) for x in blocked]))

top = 0

gap = []

for i in blocked:
	if (i[0] <= top): # we overlap
		top = max(top, i[1]+1)
		print("Increasing top to " + str(top))
	else:
		# this has been a gap
		gap.append((top, i[0]-1)) # gap, inclusive
		print("There is a gap: " + str(gap[-1]))
		top = max(top, i[1]+1)

if top < 4294967295:
	gap.append((top, 4294967295)) # final gap
	print("There is a gap: " + str(gap[-1]))
		

gapsum = 0
for y in gap:
	gapsum +	= (y[1] - y[0] + 1)

print("Total unblocked: " + str(gapsum))