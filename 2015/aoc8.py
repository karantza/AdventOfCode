import re

f = open('aoc8.txt', 'r')

total = 0
real = 0
xplod = 0
for input in f:
	input = input.rstrip()

	total = total + len(input)

	parsed = re.sub(r'^\"(.*)\"$', r'\1', input)	
	parsed = re.sub(r'\\"', '_', parsed)
	parsed = re.sub(r'\\\\', r'_', parsed)
	parsed = re.sub(r'\\x([0-9A-Fa-f]{2})', '_', parsed)
	
	real = real + len(parsed)


	xpldd = re.sub(r'\\', r'__', input)	
	xpldd = re.sub(r'"', '__', xpldd)
	xpldd = "\"" + xpldd + "\""

	xplod = xplod + len(xpldd)

	print(input + " - " + parsed + " - " + xpldd)

print (str(total) + " - " + str(real) + " = " + str(total - real))
print (str(xplod) + " - " + str(total) + " = " + str(xplod - total))
