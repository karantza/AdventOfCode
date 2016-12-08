#input = ["rect 3x2","rotate column x=1 by 1","rotate row y=0 by 4","rotate column x=1 by 1"]

grid_w = 50
grid_h = 6

# grid[y][x]
grid = [[' ' for x in range(grid_w)] for y in range(grid_h)]

def printGrid():
	for row in grid:
		print("".join(row))
	print

def rect(x,y):
	print("rect(" + str(x) + "," + str(y) + ")")
	for i in range(x):
		for j in range(y):
			grid[j][i] = '#'

def rotateRow(r, i):
	print("rotateRow(" + str(r) + "," + str(i) + ")")
	grid[r] = grid[r][-i:] + grid[r][:-i]

def rotateCol(c, i):
	print("rotateCol(" + str(c) + "," + str(i) + ")")
	col = map(lambda row: row[c], grid)
	col = col[-i:] + col[:-i]
	for j in range(len(col)):
		grid[j][c] = col[j]

def countPixels():
	return sum([l.count('#') for l in grid])

with open('Day8.txt') as input:
	for cmd in input:
		cmds = cmd.split(' ')
		if cmds[0] == 'rect':
			dims = cmds[1].split('x')
			rect(int(dims[0]), int(dims[1]))
		elif cmds[0] == 'rotate':
			if cmds[1] == 'row':
				row = int(cmds[2][2:])
				num = int(cmds[4])
				rotateRow(row, num)
			elif cmds[1] == 'column':
				col = int(cmds[2][2:])
				num = int(cmds[4])
				rotateCol(col, num)
		print(cmd)
		printGrid()

print(countPixels())
