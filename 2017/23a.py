input = open('23.txt', 'r').readlines()

input = [x.strip().split(' ') for x in input]

global lastPlayed
lastPlayed = 0

global regs
regs = {}

global pc
pc = 0

global mulcount
mulcount = 0 

def setReg(r, x):
	global regs
	regs[r] = x

def getReg(r):
	global regs
	if r not in regs:
		regs[r] = 0
	return regs[r]

def evaluate(x):
	try:
		return int(x)
	except ValueError:
		return getReg(x)


def set(x, y):
	setReg(x, evaluate(y))

def add(x, y):
	setReg(x, getReg(x) + evaluate(y))

def sub(x, y):
	setReg(x, getReg(x) - evaluate(y))

def mul(x, y):
	setReg(x, getReg(x) * evaluate(y))
	global mulcount
	mulcount += 1


def jnz(x, y):
	if evaluate(x) != 0:
		global pc
		pc += evaluate(y) - 1

execute = {
	'set': set,
	'add': add,
	'sub': sub,
	'mul': mul,
	'jnz': jnz
}

stop = False
while pc >= 0 and pc < len(input) and not stop:
	ins = input[pc]
	if len(ins) == 2:
		ins.append('')
	print 'execute[' + ins[0] + '](' + ins[1] + ', ' + ins[2] + ')'
	stop = execute[ins[0]](ins[1], ins[2])
	pc += 1
	print regs

print "multiply called: " + str(mulcount)