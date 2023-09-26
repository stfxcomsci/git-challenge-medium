
f = open("in.txt", "r")
line = f.read()
parts = line.split()
for i in range(len(parts)):
#    print(parts[i])
    parts[i] = int(parts[i])
parts.sort()
for part in parts:
    print(part, end=" ")