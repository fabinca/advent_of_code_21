with open('input.txt') as f:
    input = f.read().splitlines()

conns = []

for line in input:
    conns.append(line.split('-'))
    conns.append([line.split('-')[1], line.split('-')[0]])

#print(conns)


def find_conns(conns, last_cave, small_caves, found_conns, path):
	if len(small_caves) == len(set(small_caves)):
		duplicates = False
	else: 
		duplicates = True
	transits = [entry[1] for entry in conns if entry[0] == last_cave]
	for t in transits:
		small_caves_copy = small_caves[:]
		path_copy = path[:]
		if t not in small_caves or ((duplicates is False) and (t not in ['start', 'end'])) :
			if t == 'end':
				found_conns += 1
				print(path, duplicates, small_caves)
			else:
				if t.islower():
					small_caves_copy.append(t)
				path_copy.append(t)
				found_conns = find_conns(conns, t, small_caves_copy, found_conns, path_copy)
	return found_conns

out = find_conns(conns, 'start', ['start'], 0, ['start'])

print(out)

