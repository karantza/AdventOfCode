input = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]

target = 150

results = []

def tryContainer(i, used):
	used = list(used + [i])
	buckets = map(lambda x: input[x], used)
	total = sum(buckets)

	if (total == target):
		results.append(used)
		return
	if total > target:
		return

	for j in range(i+1, len(input)):
		if j not in used:
			tryContainer(j, used)

for i in range(0, len(input)):
	tryContainer(i, [])

minBuckets = min( map(len, results) )
bestBuckets = filter( lambda x: len(x) == minBuckets, results )

for y in bestBuckets:
	print(map(lambda x: input[x], y)) 

print(str(len(bestBuckets)) + " have " + str(minBuckets) + " containers" )
