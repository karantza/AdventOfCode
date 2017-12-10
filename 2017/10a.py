input = [70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41]

list = range(0, 256)
index = 0
skip = 0


def reverse(idx, length):
	sublist = []
	for i in range(idx, idx + length):
		sublist.append(list[i % len(list)])
	
	sublist.reverse()

	for i in range(idx, idx + length):
		list[i % len(list)] = sublist[i - idx]

for val in input:
	reverse(index, val)
	index += val + skip
	skip += 1

print list[0] * list[1]