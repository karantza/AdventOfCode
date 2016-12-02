import math

def divisors(n):
    small_divisors = [i for i in xrange(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors

total = 34000000

i = 0
while (True):
	i += 1
	d = divisors(i)
	s1 = sum(d) * 10
	s2 = sum(x for x in d if i / x <= 50) * 11

	if s2 >= total:
		print("Result!")
		print(i, s2)
		break
