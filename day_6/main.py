with open("input.txt") as file:
  data = file.read().strip('\n').split(',')
data = [int(num) for num in data]
print(data)

'''days = 80
for day in range(days):
  i = len(data) - 1
  while i >= 0:
    if data[i] == 0:
      data[i] = 7
      data.append(8)
    data[i] -= 1
    i -= 1

print(len(data))'''

fish = [0] * 9
print(fish)
for i in range(9):
  for num in data:
    if num == i:
      fish[i] += 1
print (fish)
days = 256
for day in range(days):
  j = 0
  fish_copy = fish[0]
  while j < 8:
    fish[j] = fish[j+1]
    j += 1
  fish[6] += fish_copy
  fish[8] = fish_copy

print(sum(fish))
