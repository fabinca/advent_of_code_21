# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/05 22:30:06 by cfabian           #+#    #+#              #
#    Updated: 2021/12/05 23:53:36 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

x1_data = []
x2_data = []
y1_data = []
y2_data = []
with open("input.txt", 'r') as file:
	data = file.read().splitlines()
for line in data:
	x1_data.append(int(line.split('->')[0].split(',')[0]))
	y1_data.append(int(line.split('->')[0].split(',')[1]))
	x2_data.append(int(line.split('->')[1].split(',')[0]))
	y2_data.append(int(line.split('->')[1].split(',')[1]))
max_x = max(max(x1_data), max(x2_data))
max_y = max(max(y1_data), max(y2_data))
map = [[0] * (max_x + 1) for _ in range(max_y +1 )]
	
for i in range(len(x1_data)):
	#horizontal
	if x1_data[i] == x2_data[i]:
		x = x1_data[i]
		if y1_data[i] < y2_data[i]:
			y = y1_data[i]
			while y <= y2_data[i]:
				map[y][x] += 1
				y += 1
		elif y1_data[i] > y2_data[i]:
			y = y2_data[i]
			while y <= y1_data[i]:
				map[y][x] += 1
				y += 1
	#vertical
	elif y1_data[i] == y2_data[i]:
		y = y1_data[i]
		if x1_data[i] < x2_data[i]:
			x = x1_data[i]
			while x <= x2_data[i]:
				map[y][x] += 1
				x += 1
		elif x1_data[i] > x2_data[i]:
			x = x2_data[i]
			while x <= x1_data[i]:
				map[y][x] += 1
				x += 1		

	#diagonal 
	elif x1_data[i] < x2_data[i] and y1_data[i] < y2_data[i]:
		x = x1_data[i]
		y = y1_data[i]
		while x <= x2_data[i] and y <= y2_data[i]:
			map[y][x] += 1
			x += 1
			y += 1
	elif x1_data[i] > x2_data[i] and y1_data[i] > y2_data[i]:
		x = x2_data[i]
		y = y2_data[i]
		while x <= x1_data[i] and y <= y1_data[i]:
			map[y][x] += 1
			x += 1
			y += 1
	#diagonal /
	elif x1_data[i] < x2_data[i] and y1_data[i] > y2_data[i]:
		x = x1_data[i]
		y = y1_data [i]
		while x <= x2_data[i] and y >= y2_data[i]:
			map[y][x] += 1
			x += 1
			y -= 1
	elif x1_data[i] > x2_data[i] and y1_data[i] < y2_data[i]:
		x = x1_data[i]
		y = y1_data [i]
		while x >= x2_data[i] and y <= y2_data[i]:
			map[y][x] += 1
			x -= 1
			y += 1

danger_fields = 0
for row in map:
	for num in row:
		if num >= 2:
			danger_fields += 1

print(danger_fields)