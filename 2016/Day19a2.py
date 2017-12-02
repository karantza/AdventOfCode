input = 3014603

elf = {'index':1, 'next':None}

ielf = elf
for i in range(1, input):
	e = {'index':i+1, 'next':None}
	ielf['next'] = e
	ielf = e

ielf['next'] = elf

while elf['next'] != elf:
	elf['next'] = elf['next']['next']
	elf = elf['next']

print(elf['index'])