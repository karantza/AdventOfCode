input = 376

buffer = [0]
ptr = 0

for i in range(1, 2018):
	ptr = ((ptr + input) % len(buffer)) + 1
	buffer.insert(ptr, i)

print buffer[ptr+1]