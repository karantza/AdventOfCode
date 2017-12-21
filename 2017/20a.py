import re

input = open('20-adina.txt', 'r').readlines()

pattern = re.compile(r'p=<([ \-0-9]+),([ \-0-9]+),([ \-0-9]+)>, v=<([ \-0-9]+),([ \-0-9]+),([ \-0-9]+)>, a=<([ \-0-9]+),([ \-0-9]+),([ \-0-9]+)>')

class V3:
	def __init__(self,x,y,z):
		self.x = int(x)
		self.y = int(y)
		self.z = int(z)

	def manhattan(self, pwr):
		return abs(self.x)**pwr + abs(self.y)**pwr + abs(self.z)**pwr

	def __str__(self):
		return "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"

class Particle:
	def __init__(self,i,p,v,a):
		self.i = i
		self.p = p
		self.v = v
		self.a = a


	def __str__(self):
		return "#" + str(self.i) + " p=" + str(self.p) + ", v=" + str(self.v) + ", a=" + str(self.a)

def parse(i,s):
	m = pattern.match(s).groups()
	p = V3(m[0],m[1],m[2])
	v = V3(m[3],m[4],m[5])
	a = V3(m[6],m[7],m[8])
	return Particle(i,p,v,a)

particles = [parse(i,x) for i,x in enumerate(input)]


particles.sort(key=lambda p: p.p.manhattan(1))
particles.sort(key=lambda p: p.v.manhattan(1))
particles.sort(key=lambda p: p.a.manhattan(2))

print(str(particles[0]))
