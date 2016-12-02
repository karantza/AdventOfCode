import re

info = {}

f = open('aoc13.txt')
for s in f:
	x = re.search(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', s)
	score = int(x.group(3))
	if (x.group(2) == 'lose'):
		score = -score
	a = x.group(1)
	b = x.group(4)
	if a not in info:
		info[a] = {}
	info[a][b] = score

names = info.keys()

info['me'] = {}
for n in names:
	info[n]['me'] = 0
	info['me'][n] = 0

names = info.keys()

seatings = []

def seat(s, all):
	if len(s) == len(names):
		seatings.append(s)
		return
	for x in names:
		if x not in s:
			seat(s + [x], all)

for x in names:
	seat([x], seatings)

def score(s):
	r = 0
	for i in range(len(s)):
		j = (i + 1) % len(s)
		r += info[s[i]][s[j]]
		r += info[s[j]][s[i]]
	return r

scores = map(score, seatings)
print max(scores)

