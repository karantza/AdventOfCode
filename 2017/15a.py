input = [703, 516]
fac = [16807,48271]

def generate(prev, factor):
	return (prev * factor) % 2147483647

prev = input

count = 0
for i in range(0, 40000000):
	prev = [generate(prev[x], fac[x]) for x in [0,1]]
	low = [prev[x] & 0xffff for x in [0,1]]	
	
	if low[0] == low[1]:
		count += 1
	
	if (i % 1000 == 0):
		print (i, count)

print 'final: ' + str(count)