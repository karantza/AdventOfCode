input = [int(x) for x in open('5.txt', 'r').readlines()]

pc = 0
count = 0

while (pc < len(input)):
	count = count + 1 # counting steps
	jump = input[pc] # how far to go
	if (jump >= 3):
		input[pc] = jump - 1 # decrement if jump >= 3
	else:
		input[pc] = jump + 1 # increment where we are
	pc = pc + jump # jump

print count