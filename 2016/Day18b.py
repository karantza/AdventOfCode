input = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^"

rows = 400000

prev = input
safecount = input.count('.')

#print(input)

for r in range(1, rows):
	prev = "." + prev + "."
	new = ""
	for c in range(0, len(input)):
		nbhd = prev[c:c+3]

		if nbhd == "^^." or nbhd == ".^^" or nbhd == "^.." or nbhd == "..^":
			new = new + "^"
		else:
			new = new + "."

	safecount += new.count('.')
	prev = new
	#print(new)

print(safecount)


