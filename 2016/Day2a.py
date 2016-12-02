pad = [[1,2,3],[4,5,6],[7,8,9]]
coord = [1,1]

code = ""

with open('Day2.txt', 'r') as file:
    for sequence in file: 
    	for d in sequence:
    		if d == 'L':
    			coord[0] = coord[0] - 1
    		elif d == 'R':
    			coord[0] = coord[0] + 1
       		elif d == 'D':
    			coord[1] = coord[1] + 1
    		elif d == 'U':
    			coord[1] = coord[1] - 1

    		if coord[0] < 0:
    			coord[0] = 0
    		if coord[1] < 0:
    			coord[1] = 0

    		if coord[0] > 2:
    			coord[0] = 2
    		if coord[1] > 2:
    			coord[1] = 2

    	code = code + str(pad[coord[1]][coord[0]])

    print(code)