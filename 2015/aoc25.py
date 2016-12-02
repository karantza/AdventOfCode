import sys
input=(3075, 2981)


def address(x,y):
	index = 1
	for i in range(1,y):
		index += i

	for i in range(1,x):
		index += i+y

	return index

def iterate(i):
	code = 20151125
	for j in range(1, i):
		code *= 252533
		code = code % 33554393
	return code

def test():
	for y in range(1, 7):
		for x in range(1, 7):
			sys.stdout.write(str(iterate(address(x,y))) + '\t')
		print('')

index = address(input[0],input[1])
print("index: " + str(index))

code = iterate(index)
print("code: " + str(code))
