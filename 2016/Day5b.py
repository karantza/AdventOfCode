import hashlib
def md5(x):
	return hashlib.md5(x).hexdigest()

input = "wtnhxymk"
#input = "abc"

i = 0
code = list("????????")
while code.count("?") > 0:
	m = md5(input + str(i))

	if i % 1000000 == 0: 
		print(i)
	
	if m[:5] == "00000":
		indexstr = m[5]
		value = m[6]
		if indexstr in "01234567":
			index = int(indexstr)
			if code[index] == "?":
				code[index] = value
				print ("Code: " + "".join(code))
	i += 1

print("Final code: " + "".join(code))
