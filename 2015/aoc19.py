
medicine = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
medicine = "ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPBSiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCaSiRnFYFArSiRnMgArCaSiRnPTiTiBFYPBFArSiRnCaSiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFArSiRnCaCaFArRnCaFArCaSiRnSiRnMgArFYCaSiRnMgArCaCaSiThPRnFArPBCaSiRnMgArCaCaSiThCaSiRnTiMgArFArSiThSiThCaCaSiRnMgArCaCaSiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPBCaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiBSiRnFYFArCaCaPRnFArPBCaCaPBSiRnTiRnFArCaPRnFArSiRnCaCaCaSiThCaRnCaFArYCaSiRnFArBCaCaCaSiThFArPBFArCaSiRnFArRnCaCaCaFArSiRnFArTiRnPMgArF"

#replacements = [('e','H'),('e','O'),('H','HO'),('H','OH'),('O','HH')]
#medicine =  'HOHOHO'

def step(input):
	results = set()

	for i in range(len(input)):
		for r in replacements:
			if input[i:].startswith(r[0]):
				l = len(r[0])
				results.add(input[:i] + r[1] + input[i+l:])

	return results

fabSteps = []
fabCache = {}

Inf = float("inf")

def fabricate(input, depth):

	if input in fabCache:
		if fabCache[input] == Inf:
			return Inf # We know that the answer isn't in here
		d = fabCache[input] + depth
		print("Found existing route of depth " + str(d))
		fabSteps.append(d)

	if input == medicine:
		print ("Found medicine after " + str(depth) + " steps")
		return depth

	results = step(input)

	bestDepth = Inf
	for x in results:

		if len(x) > len(medicine):
			continue
		
		y = fabricate(x, depth + 1)
		if (y != Inf):
			print("Found " + str(y-depth-1) + " steps after: " + x[:50])
			fabCache[x] = y - depth - 1
			bestDepth = min(bestDepth, y)
		else:
			print("No medicine at " + str(depth) + " under " + x[:50])
			fabCache[x] = Inf		
	return bestDepth

#fabricate('e', 0)
#print("fewest steps: " + str(min(fabSteps)))

elements = []
for i in range(len(medicine)):
	if medicine[i].islower():
		continue

	if i+1 < len(medicine) and medicine[i+1].islower():
		elements.append(medicine[i:i+2])
	else:
		elements.append(medicine[i:i+1])

print (elements)

def replace(x):
	if x == 'Rn':
		return '('
	if x == 'Ar':
		return ')'
	if x == 'Y':
		return ','
	return 'X'

elements = map(replace, elements)

print(''.join(elements))

a = (len(elements))
b = (len(filter(lambda x: x == '(' or x == ')',elements)))
c = (len(filter(lambda x: x == ',',elements)))
print(a, b, c)
print(a - b - 2*c - 1)

