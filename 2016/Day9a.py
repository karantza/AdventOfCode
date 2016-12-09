

with open("Day9.txt") as file:
	input = file.read()

#input = "X(8x2)(3x3)ABCY"

i = 0
output = ""
while i < len(input):
	if input[i] == "(":
		l1 = input[i+1:].find("x")
		span = int(input[i+1:i+1+l1])
		l2 = input[i+1+l1:].find(")")
		copy = int(input[i+1+l1+1:i+1+l1+l2])
		i += l1 + l2 + 2 
		
		for j in range(copy):
			output += input[i:i+span]

		i += span
	else:
		output += input[i]
		i += 1

print len(output)