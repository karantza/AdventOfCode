pad = [ ['x','x','x','1','x','x','x'],
		['x','x','2','3','4','x','x'],
		['x','5','6','7','8','9','x'],
		['x','x','A','B','C','x','x'],
		['x','x','x','D','x','x','x']]
coord = [1,2]

code = ""

with open('Day2.txt', 'r') as file:
    for sequence in file: 
    	for d in sequence:
    		
    		newc = coord[:]

    		if d == 'L':
    			newc[0] = newc[0] - 1
    		elif d == 'R':
    			newc[0] = newc[0] + 1
       		elif d == 'D':
    			newc[1] = newc[1] + 1
    		elif d == 'U':
    			newc[1] = newc[1] - 1

    		if newc[1] < 0 or newc[1] > 4: # above or below
    			continue

    		if pad[newc[1]][newc[0]] == 'x': # too far to the side
    			continue

    		coord = newc[:]

    	code = code + str(pad[coord[1]][coord[0]])

    print(code)