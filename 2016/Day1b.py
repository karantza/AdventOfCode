import sys

with open('Day1.txt', 'r') as file:
    input=file.read()

inst = input.split(', ')
currentDir = 'N'
coord = [0,0]

visited = {}

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

	for i in range(0,dist):
		# and move there
		if currentDir == 'N':
			coord[1] = coord[1]-1
		elif currentDir == 'S':
			coord[1] = coord[1]+1
		elif currentDir == 'W':
			coord[0] = coord[0]-1
		elif currentDir == 'E':
			coord[0] = coord[0]+1

		currentCoord = coord[0], coord[1]
		if (currentCoord in visited):
			print(str(currentCoord) + " visited twice, distance: " + str(sum(map(abs, coord))))
			sys.exit(0)
		else:
			visited[currentCoord] = True

