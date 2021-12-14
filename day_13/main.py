with open("input.txt") as f:
  data = f.read().splitlines()

dots = []
folds = []
x_max = 0
y_max = 0
for line in data:
  if "," in line:
    x = int(line.split(',')[0])
    y = int(line.split(',')[1])
    dots.append([x,y])
  elif "fold" in line:
    axis = line.split("=")[0][-1]
    num = int(line.split("=")[1])
    folds.append([axis, num])

print(dots)
print(folds)
for line in folds: 
  fold = line[1]
  for dot in dots:
    if line[0] == 'y':
      if dot[1] >= fold:
       dot[1] = fold -(dot[1] - fold)
    elif line[0] == 'x':
      if dot[0] >= fold:
       dot[0] = fold -(dot[0] - fold)

unique_dots = []
for dot in dots:
  if dot not in unique_dots:
    unique_dots.append(dot)
x_folds = [line[1] for line in folds if line[0] == 'x']
y_folds = [line[1] for line in folds if line[0] == 'y']
x_max = min(x_folds)
y_max = min(y_folds)

dot_map =  [[0 for i in range(x_max)] for j in range(y_max)]
for x,y in dots:
  dot_map[y][x] = 1

for line in dot_map:
  print(line)


print(unique_dots, "\n", len(unique_dots))




'''dot_map =  [[0 for i in range(x_max + 1)] for j in range(y_max + 1)]
for x,y in dots:
  dot_map[y][x] = 1

#for line in dot_map:
  #print(line)

for line in folds:
  if line[0] == 'y':
    fold = line [1]
    for y in range (fold + 1, y_max + 1):
      for x in range (x_max + 1):
        if dot_map[y][x] == 1:
          dot_map[y - fold - 1][x] = 1  
          dot_map[y][x] = 0
    y_max = fold - 1
    print(line)
  elif line[0] == 'x':
    fold = line [1]
    for x in range (fold + 1, x_max + 1):
      for y in range (y_max + 1):
        if dot_map[y][x] == 1:
          dot_map[y][x - fold - 1] = 1  
          dot_map[y][x] = 0
    x_max = fold - 1
    print(line)
  break

print('\n')
count = 0
for x,y in dot_map:
  count += sum(line)'''

#print(count)
