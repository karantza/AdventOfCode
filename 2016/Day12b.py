input = ["cpy 41 a",
"inc a",
"inc a",
"dec a",
"jnz a 2",
"dec a"]

reg = {'a':0, 'b':0, 'c':1, 'd':0}

i = 0

count = 0

with open("Day12.txt") as file:
	input = file.readlines()

def val(x):
	try:
		return int(x)
	except ValueError:
		return reg[x]

while i < len(input):
	line = input[i].strip()
	count += 1
 	o = i
	ins = line.split(" ")
	if ins[0] == "cpy":
		x = val(ins[1])
		y = ins[2]
		reg[y] = x
		i += 1
	elif ins[0] == "inc":
		x = ins[1]
		reg[x] += 1
		i += 1
	elif ins[0] == "dec":
		x = ins[1]
		reg[x] -= 1
		i += 1
	elif ins[0] == "jnz":
		x = val(ins[1])
		y = ins[2]
		
		if x != 0:
			i += int(y)
		else:
			i += 1

	#print("exec ins " + str(o) + ": " + line + ", after: " + str(reg))

print("Halted after " + str(count) + ": " + str(reg))
