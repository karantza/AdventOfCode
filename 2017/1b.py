input = open('1.txt', 'r').read()

valid = []

step = len(input) / 2

for i,c in enumerate(input):
	ni = (i + step) % len(input)
	n = input[ni]
	if c == n:
		valid.append(int(c))

print(sum(valid))