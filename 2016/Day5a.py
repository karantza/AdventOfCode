import hashlib
def md5(x):
	return hashlib.md5(x).hexdigest()

input = "wtnhxymk"

i = 0
code = ""
while len(code) < 8:
	m = md5(input + str(i))

	if i % 1000000 == 0: 
		print(i)
	
	if m[:5] == "00000":
		code += m[5]
		print ("Code: " + code)
	i += 1



print(code)
