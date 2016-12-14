import hashlib
import re

def md5(x):
	return hashlib.md5(x).hexdigest()

re_triple = re.compile(r"(.)\1{2}")
re_pentuples = re.compile(r"(.)\1{4}")

input = "yjdafjpo"

keys = set() # established keys
triples = {} # map of letter to the index it has a triple in

i = 0

def addTo(dict, key, val):
	if key not in dict:
		dict[key] = []
	dict[key].append(val)

def hash(i):
	value = md5(input + str(i))
	for x in range(1, 2017):
		value = md5(value)
	return value

maxCheckedKey = 0
keyCount = 0
while True:

	h = hash(i)
	tmatch = re_triple.search(h)
	pmatch = re_pentuples.findall(h)

	for p in pmatch:
		# check if any triples in the past thousand match this character, if so promote them to keys
		print("Found a pentuple at " + str(i) + ": " + p[0])
		maxCheckedKey = (i-1000)
		for t in triples[p[0]]:
			if t > maxCheckedKey:
				keys.add(t)
				print("Adding verified key at " + str(t))

		keyCount = len([x for x in keys if x < maxCheckedKey])

		print("Verified key count: " + str(keyCount) + ", threshold = " + str(maxCheckedKey))


	if keyCount > 64:
		print("Keys:\n" + str(keys))
		skeys = sorted(list(keys))
		print("Sufficient keys found! 64th key is at index " + str(skeys[63]))
		break

	if tmatch:
		addTo(triples, tmatch.group()[0], i)

	i += 1



