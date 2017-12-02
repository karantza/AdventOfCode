input = 3014603

i = 1
j = 1

laststep = 1

steps = ['1']

for i in range(1, input+1):
	if (j + 1) < laststep:
		j += 1
	else: 
		j += 2

	if j > i:
		laststep = i
		steps.append(str(i))
		j = 1

	if (i % int(input / 100) == 0):
		print(str(100 * i / input) + "%...")

print(",".join(steps))
print("winner: " + str((i,j)))