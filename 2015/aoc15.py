input = [("Sprinkles",5,-1,0,0,5), 
("PeanutButter",-1,3,0,0,1), 
("Frosting",0,-1,4,0,6), 
("Sugar",-1,0,0,2,8)]

scores = []

for a in range(0, 100):
	for b in range(0, 100 - a):
		for c in range(0, 100 - a - b):
			d = 100 - a - b - c

			calories = 	a * input[0][5] + b * input[1][5] + c * input[2][5] + d * input[3][5]

			if (calories != 500):
				continue
				
			props = [
				a * input[0][1] + b * input[1][1] + c * input[2][1] + d * input[3][1],
				a * input[0][2] + b * input[1][2] + c * input[2][2] + d * input[3][2],
				a * input[0][3] + b * input[1][3] + c * input[2][3] + d * input[3][3],
				a * input[0][4] + b * input[1][4] + c * input[2][4] + d * input[3][4]
			]


			score = reduce(lambda x,y: x * max(0,y), props, 1)
			scores.append(score)

print(scores)

print(max(scores))