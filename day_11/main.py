# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/11 22:39:13 by cfabian           #+#    #+#              #
#    Updated: 2021/12/11 23:31:08 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

SIZE = 10
#steps = 195

with open("input.txt") as file:
	data = file.read().splitlines()
print(data)
octopusses = []
for line in data:
	octopusses.append([int(let) for let in line])
for line in octopusses:
	print(line)

print("\n")

def octo_flash(octopusses, row, col):
	for line in octopusses:
		print(line)
	print(f"row = {row} col = {col}")
	print('\n')
	for i in [-1, 0 , 1]:
		for j in [-1, 0, 1]:
			if (0 <= row + i < SIZE) and (0 <= col + j < SIZE) and (i != 0 or j != 0):
				octopusses[row + i][col + j] += 1
				if octopusses[row + i][col + j] == 10:
					octo_flash(octopusses, row + i, col + j)


flashes = 0
steps = 0
while True:
	steps += 1
	flashes_per_step = 0
	#increase num
	for row in range(SIZE):
		for col in range(SIZE):
			octopusses[row][col] += 1
			if octopusses[row][col] == 10:
				octo_flash(octopusses, row, col)
	#count flashes & set octo to 0
	for row in range(SIZE):
		for col in range(SIZE):
			if octopusses[row][col] > 9:
				octopusses[row][col] = 0
				flashes_per_step += 1
	flashes += flashes_per_step
	#see if synchronized
	if flashes_per_step == SIZE*SIZE:
		print(steps)
		break

for line in octopusses:
	print(line)

print(flashes)
				
