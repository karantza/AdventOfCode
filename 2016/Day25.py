input = []
with open("Day25.txt") as f:
	input = [x.strip() for x in f.readlines()]

reference = "0101010101"

def executeWithA(a):
	reg = {'a':0, 'b':0, 'c':0, 'd':0}

	reg['a'] = a
	i = 0

	output = ""

	count = 0

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
		elif ins[0] == 'out':
			output += str(val(ins[1]))
			if len(output) > 10:
				print(str(a) + " correct")
				return True
			else:
				if output != reference[:len(output)]:
					#print(str(a) + " failed")
					return False

			i += 1
		else:
			print("invalid: " + str(ins))

	print("Final output: " + output)

a = 1
done = False
while not done:
	done = executeWithA(a)
	a += 1


