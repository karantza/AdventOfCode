input = open('4.txt', 'r').readlines()

def check(s):
	arr = [''.join(sorted(x)) for x in s.split()]
	return len(arr) == len(set(arr))

print len(filter(check, input))