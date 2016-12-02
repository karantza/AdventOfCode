input = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"

inst = input.split(', ')
currentDir = 'N'
coord = [0,0]

turn = {
	'N': {'R':'E','L':'W'},
	'S': {'R':'W','L':'E'},
	'E': {'R':'S','L':'N'},
	'W': {'R':'N','L':'S'}
}


for value in inst:
	direction = value[0]
	dist = int(value[1:])

	# turn to face a new direction
	currentDir = turn[currentDir][direction]

	# and move there
	if currentDir == 'N':
		coord[1] = coord[1]-dist
	elif currentDir == 'S':
		coord[1] = coord[1]+dist
	elif currentDir == 'W':
		coord[0] = coord[0]-dist
	elif currentDir == 'E':
		coord[0] = coord[0]+dist

	print(value, coord)

print("distance: ", sum(coord))
