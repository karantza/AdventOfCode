import re

input = "3113322113"

seq = re.compile(r'^(\d)\1*')

def lookandsay(s):
	result = ""
	while (len(s) > 0):
		myseq = seq.match(s).group(0)
		result += str(len(myseq)) + myseq[0]
		s = s[len(myseq):]
	return result

for x in xrange(50):
	input = lookandsay(input)
	print len(input)
