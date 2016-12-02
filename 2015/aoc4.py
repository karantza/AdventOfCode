import hashlib

prefix = "ckczppom"

def mine(x):
	i = 1
	while True:
		key = prefix + str(i)
		md5 = hashlib.md5(key).hexdigest()
		if md5.startswith(x):
			break
		i = i + 1

	print(str(i) + " = " + md5)
	

mine("00000")
mine("000000")
