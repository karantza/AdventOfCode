
input = open('1.txt', 'r').read()

valid = []

for i,c in enumerate(input):
	ni = (i + 1) % len(input)
	n = input[ni]
	if c == n:
		valid.append(int(c))

print(sum(valid))