input = [703, 516]

fac = [16807,48271]

matte = [0b11, 0b111]

def generate(prev, factor):
	return (prev * factor) % 2147483647

count = 0
numTests = 5000000

def getSequence(i):
	prev = input[i]
	results = []
	c = 0
	while c < numTests:
		prev = generate(prev, fac[i])
		if prev & matte[i] == 0:
			results.append(prev & 0xffff)
			c += 1
	return results

generated = [getSequence(0), getSequence(1)]


seqLen = min([len(x) for x in generated])

for i in range(0, seqLen):
	if generated[0][i] == generated[1][i]:
		count += 1

print 'final: ' + str(count)