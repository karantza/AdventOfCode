input = 376

ptr = 0

valAfterZero = 0

for i in range(1, 50000000):
	ptr = ((ptr + input) % i) + 1
	if ptr == 1:
		valAfterZero = i

print valAfterZero