import re
from collections import Counter

input = open('20.txt', 'r').readlines()
#input = ['p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>','p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>','p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>','p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>']

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

	def __add__(self, other):
		return V3(self.x + other.x, self.y + other.y, self.z + other.z)

class Particle:
	def __init__(self,i,p,v,a):
		self.i = i
		self.p = p
		self.v = v
		self.a = a

	def step(self):
		self.v = self.v + self.a
		self.p = self.p + self.v

	def __str__(self):
		return "#" + str(self.i) + " p=" + str(self.p) + ", v=" + str(self.v) + ", a=" + str(self.a)


def parse(i,s):
	m = pattern.match(s).groups()
	p = V3(m[0],m[1],m[2])
	v = V3(m[3],m[4],m[5])
	a = V3(m[6],m[7],m[8])
	return Particle(i,p,v,a)

particles = [parse(i,x) for i,x in enumerate(input)]
lastchange = 0
i = 0;

while i - lastchange < 100:
	for p in particles:
		p.step()

	start = len(particles)

	# resolve collisions
	positions = Counter(str(p.p) for p in particles)
	collisions = [x for x,c in positions.most_common() if c > 1]
	if len(collisions) > 0:
		particles = [p for p in particles if str(p.p) not in collisions]
		end = len(particles)
		if (start != end):
			lastchange = i
	i += 1

print str(len(particles)) + " remain after " + str(i) + " iterations"

