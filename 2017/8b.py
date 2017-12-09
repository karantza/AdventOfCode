import re

#input = ["b inc 5 if a > 1","a inc 1 if b < 5","c dec -10 if a >= 1","c inc -20 if c == 10"]
input = open('8.txt', 'r').readlines()

registers = {}
def getReg(x):
	if x not in registers:
		registers[x] = 0

	return registers[x]

def setReg(x, val):
	registers[x] = val
	
testConditions = {
	">=": lambda a,b: a >= b, 
	"<=": lambda a,b: a <= b, 
	">": lambda a,b: a > b, 
	"<": lambda a,b: a < b, 
	"==": lambda a,b: a == b, 
	"!=": lambda a,b: a != b,
}

operations = {
	"inc": lambda reg, x: setReg(reg, getReg(reg) + x),
	"dec": lambda reg, x: setReg(reg, getReg(reg) - x)
}

class Instruction:
	def __init__(self, match):
		self.txt = match.group(0)
		self.register = match.group(1)
		self.operation = operations[match.group(2)]
		self.value = int(match.group(3))
		self.test = match.group(4)
		self.condition = testConditions[match.group(5)]
		self.testvalue = int(match.group(6))

	def execute(self):
		# test condition
		toTest = getReg(self.test)
		if self.condition(toTest, self.testvalue):
			# execute instruction
			self.operation(self.register, self.value)


expr = re.compile(r"(\w+) (\w+) (-?\d+) if (\w+) (>=|<=|<|>|==|!=) (-?\d+)")

instructions = [Instruction(expr.match(i)) for i in input]

maxval = 0
for i in instructions:
	i.execute()
	maxval = max([maxval] + registers.values())

print "largest value ever held: " + str(maxval)

