rows = []

with open('Day3.txt', 'r') as file:
    total = 0
    for triangestr in file:
        t = [int(i) for i in triangestr.split()]
        rows.append(t)

for i in range(0, len(rows), 3):
    for j in range(0,3):
        t = [rows[i][j],rows[i+1][j],rows[i+2][j]]

        if ((t[0]+t[1])>t[2] and (t[0]+t[2])>t[1] and (t[1]+t[2])>t[0]):
            total = total + 1
            print("ok " + str(t))
        else:
            print("bad " + str(t))
print (total)
