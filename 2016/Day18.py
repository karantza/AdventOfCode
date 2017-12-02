input = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^"

rows = 40

board = [input]

for r in range(1, rows):
	prev = "." + board[r-1] + "."
	new = ""
	for c in range(0, len(input)):
		nbhd = prev[c:c+3]

		if nbhd == "^^." or nbhd == ".^^" or nbhd == "^.." or nbhd == "..^":
			new = new + "^"
		else:
			new = new + "."

	board.append(new)

print "\n".join(board)

print("".join(board).count("."))
