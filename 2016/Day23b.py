import locale
locale.setlocale(locale.LC_ALL, 'en_US')

input = ["cpy 2 a",
"tgl a",
"tgl a",
"tgl a",
"cpy 1 a",
"dec a",
"dec a"]


reg = {'a':12, 'b':0, 'c':0, 'd':0}

i = 0
count = 0

with open("Day23.txt") as file:
	input = file.readlines()


code = [x.strip().split(' ') for x in input]


def val(x):
	try:
		return int(x)
	except ValueError:
		return reg[x]

while i < len(code):# and count < 1000000:
	count += 1
 	o = i
	ins = code[i]
	if ins[0] == "cpy":
		x = val(ins[1])
		y = ins[2]
		if y in reg:
			reg[y] = x
		i += 1
	elif ins[0] == "inc":
		x = ins[1]
		if x in reg:
			reg[x] += 1
		i += 1
	elif ins[0] == "dec":
		x = ins[1]
		if x in reg:
			reg[x] -= 1
		i += 1
	elif ins[0] == "jnz":
		x = val(ins[1])
		y = val(ins[2])
		
		if x != 0:
			i += y
		else:
			i += 1

	elif ins[0] == "tgl":
		x = val(ins[1])
		t = i + x

		if t >= len(code) or t < 0:
			i += 1
			continue

		if len(code[t]) == 2: # 1 arg instruction
			if code[t][0] == 'inc':
				code[t][0] = 'dec'
			else:
				code[t][0] = 'inc'
		else: # 2 arg instruction
			if code[t][0] == 'jnz':
				code[t][0] = 'cpy'
			else:
				code[t][0] = 'jnz'
		i += 1


	if count % 100000 == 0:
		print("count: " + locale.format("%d", count, grouping=True))
		#print(str(count) + " exec ins " + str(o) + ": " + str(ins) + ", after: " + str(reg))

print("Halted after " + str(count) + ": " + str(reg))
