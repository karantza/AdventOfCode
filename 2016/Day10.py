
with open("Day10.txt") as file:
	input = file.readlines()

# input = ["value 5 goes to bot 2",
# "bot 2 gives low to bot 1 and high to bot 0",
# "value 3 goes to bot 1",
# "bot 1 gives low to output 1 and high to bot 0",
# "bot 0 gives low to output 2 and high to output 0",
# "value 2 goes to bot 2"]

bots = {}
botDest = {}
outputs = {}

def addToBot(botid, value):
	if botid in bots:
		bots[botid].append(value)
	else:
		bots[botid] = [value]

for line in input:
	words = line.split(' ')
	if words[0] == "value":
		value = int(words[1])
		botid = int(words[5])
		addToBot(botid, value)
	elif words[0] == "bot":
		botid = int(words[1])
		lowout = words[5] == "output" # true if output, false if bot
		lowid = int(words[6])
		hiout = words[10] == "output" 
		hiid = int(words[11])
		botDest[botid] = {"lowout":lowout, "lowid":lowid, "hiout":hiout, "hiid":hiid}

while True: 
	filtered = [x for x in bots if len(bots[x]) == 2]
	if len(filtered) == 0:
		break

	for botid in filtered:
		
		hi = max(bots[botid])
		low = min(bots[botid])

		if (hi == 61 and low == 17):
			print("solution 1: bot " + str(botid))

		dest = botDest[botid]

		if dest["lowout"]:
			outputs[dest["lowid"]] = low
		else:
			addToBot(dest["lowid"], low)

		if dest["hiout"]:
			outputs[dest["hiid"]] = hi
		else:
			addToBot(dest["hiid"], hi)

		del bots[botid]

print("solution 2: " + str(outputs[0] * outputs[1] * outputs[2]))
