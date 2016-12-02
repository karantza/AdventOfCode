
f = open('aoc23.txt', 'r')

ins = []

for line in f:
	ins.append({'op':line[:3], 'args':line[4:-1].split(', '), 'txt':line[:-1]})

i = 0
reg = {'a':1, 'b':0}

while i < len(ins):
	op = ins[i]['op']
	arg = ins[i]['args']

	print(str(i) + ": " + ins[i]['txt'] + ", " + str(reg))

	if op == 'hlf':
		reg[arg[0]] = int(reg[arg[0]] / 2)
	elif op == 'tpl':
		reg[arg[0]] *= 3
	elif op == 'inc':
		reg[arg[0]] += 1
	elif op == 'jmp':
		i += int(arg[0])
		continue
	elif op == 'jie':
		if (reg[arg[0]] % 2 == 0):
			i += int(arg[1])
			continue
	elif op == 'jio':
		if (reg[arg[0]] == 1):
			i += int(arg[1])
			continue
	else:
		print("Error!")

	i += 1

print(reg)