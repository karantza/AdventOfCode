
input = open('2.txt', 'r').readlines()

def evalLine(s):
	nums = ([int(x) for x in s.split()])
	nums.sort()
	nums.reverse()
	for i in range(0, len(nums)):
		for j in range(i+1, len(nums)):
			if (nums[i] % nums[j] == 0):
				return nums[i] / nums[j]


print(sum([evalLine(x) for x in input]))
