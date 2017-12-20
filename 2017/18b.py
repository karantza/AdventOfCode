from collections import deque

input = open('18.txt', 'r').readlines()

input = [x.strip().split(' ') for x in input]

class VM: 
	
	def setReg(self, r, x):
		self.regs[r] = x

	def getReg(self, r):
		if r not in self.regs:
			self.regs[r] = 0
		return self.regs[r]

	def evaluate(self, x):
		try:
			return int(x)
		except ValueError:
			return self.getReg(x)

	def snd(self, x, y):
		self.otherQueue.appendleft(self.evaluate(x))
		print(self.name + " sends " + str(self.evaluate(x)))
		self.pc += 1
		self.sendCount += 1
		return True

	def set(self, x, y):
		self.setReg(x, self.evaluate(y))
		self.pc += 1
		return True

	def add(self, x, y):
		self.setReg(x, self.getReg(x) + self.evaluate(y))
		self.pc += 1
		return True

	def mul(self, x, y):
		self.setReg(x, self.getReg(x) * self.evaluate(y))
		self.pc += 1
		return True

	def mod(self, x, y):
		self.setReg(x, self.getReg(x) % self.evaluate(y))
		self.pc += 1
		return True

	def rcv(self, x, y):
		if len(self.queue) > 0:
			val = self.queue.pop()
			self.setReg(x, val)
			self.pc += 1
			return True
		else:
			# waiting on value
			return False


	def jgz(self, x, y):
		if self.evaluate(x) > 0:
			self.pc += self.evaluate(y)
		else:
			self.pc += 1
		return True

	def __init__(self, name):
		self.name = name
		self.execute = {
			'snd': self.snd,
			'set': self.set,
			'add': self.add,
			'mul': self.mul,
			'mod': self.mod,
			'rcv': self.rcv,
			'jgz': self.jgz
		}
		self.lastPlayed = 0
		self.regs = {}
		self.pc = 0
		self.queue = deque()
		self.otherQueue = None
		self.sendCount = 0


	# returns false if waiting or out of bounds, true if execution can continue
	def step(self):
		if self.pc < 0 or self.pc >= len(input):
			return False

		ins = input[self.pc]
		if len(ins) == 2:
			ins.append('')
		#print self.name + ':' + str(self.pc) + ': execute[' + ins[0] + '](' + ins[1] + ', ' + ins[2] + ')'
		return self.execute[ins[0]](ins[1], ins[2])

duet = [VM('0'), VM('1')]
duet[0].otherQueue = duet[1].queue
duet[1].otherQueue = duet[0].queue
duet[1].setReg('p', 1)

execount = None
while execount != [0,0]:
	execount = [0,0]
	# step until we have to wait
	while duet[0].step():
		execount[0] += 1
	# step until we have to wait
	while duet[1].step():
		execount[1] += 1

print 'final send count: ' + str(duet[1].sendCount)
