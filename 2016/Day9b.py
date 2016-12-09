

with open("Day9.txt") as file:
	input = file.read()

#input = "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"

cache = {}

def decompressString(str):
	if str in cache:
		return cache[str]

	output = ""
	i = 0
	while i < len(str):
		if str[i] == "(":
			l1 = str[i+1:].find("x")
			span = int(str[i+1:i+1+l1])
			l2 = str[i+1+l1:].find(")")
			copy = int(str[i+1+l1+1:i+1+l1+l2])
			i += l1 + l2 + 2 
			
			for j in range(copy):
				output += decompressString(str[i:i+span])

			i += span
		else:
			output += str[i]
			i += 1
			
	cache[str] = output
	return output

print len(decompressString(input))