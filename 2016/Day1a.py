with open('Day1.txt', 'r') as file:
    input=file.read()

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

print("distance: ", sum(map(abs, coord)))
