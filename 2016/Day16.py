from string import maketrans

space1 = 272
space2 = 35651584
input = "10111100110001111"

def dragonCurve(a):
	tx = maketrans('01', '10')
	b = a[::-1].translate(tx)
	return a + '0' + b

def checksumStep(x):
	pairs = [x[i:i+2] for i in range(0, len(x), 2)]
	return "".join(['1' if i[0] == i[1] else '0' for i in pairs])

def evaluate(input, space):
	while len(input) < space:
		input = dragonCurve(input)

	input = input[:space]

	cksum = input
	while True:
		cksum = checksumStep(cksum)
		if len(cksum) % 2 == 1:
			break

	print(cksum)

evaluate(input, space1)
evaluate(input, space2)