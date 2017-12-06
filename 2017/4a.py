input = open('4.txt', 'r').readlines()

def check(s):
	arr = s.split()
	return len(arr) == len(set(arr))

print len(filter(check, input))