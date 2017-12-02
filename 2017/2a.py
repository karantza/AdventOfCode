
input = open('2.txt', 'r').readlines()

def evalLine(s):
	nums = [int(x) for x in s.split()]
	return max(nums) - min(nums)

print(sum([evalLine(x) for x in input]))