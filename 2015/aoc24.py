input = list(reversed([1,2,3,7,11,13,17,19,23,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]))
#input = list(reversed([1,2,3,4,5,7,8,9,10,11]))

numcompartments = 4

volume = sum(input)/numcompartments


group1 = []
minpackage = len(input)

def doesGroupHaveVolume(input, group, i):
	s = sum(group)
	if s > volume:
		return False
	if s == volume:
		return True
	for j,x in enumerate(input[i:]):
		if doesGroupHaveVolume(input, group + [x], i+j+1):
			return True


def findGroups(group, i):
	global minpackage

	if group:
		s = sum(group)

		if s > volume:
			return
		if len(group) > minpackage:
			return
		if s == volume:
			remainder = [x for x in input if x not in group]
			if doesGroupHaveVolume(remainder, [], 0):
				# this group can be divided in two evenly
				print("Found group: " + str(group))
				group1.append(group)
				minpackage = len(group)

	for j,x in enumerate(input[i:]):
		findGroups(group + [x], i+j+1)


def product(x):
	return reduce(lambda y,z: y * z, x)


findGroups([],0)

for x in group1:
	print("Candidate group: " + str(x) + " QE:" + str(product(x)))

minqe = min(map(lambda x: reduce(lambda y,z: y * z, x), group1))

print("Best QE value: " + str(minqe))

