# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/09 09:48:31 by cfabian           #+#    #+#              #
#    Updated: 2021/12/09 12:28:16 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


with open("input.txt") as file:
	data = file.read().split(" ")
	
risk_level_sum = 0
low_points = []
basin_sizes = []
for row in range(len(data)):
	for col in range(len(data[row])):
		if row == 0 or data[row-1][col] > data[row][col]:
			if row == len(data) - 1 or data[row+1][col] > data[row][col]:
				if col == 0 or data[row][col - 1] > data[row][col]:
					if col == len(data[row])-1 or data[row][col + 1] > data[row][col]:
						risk_level_sum += int(data[row][col]) + 1
						low_points.append([row, col])					

print(low_points)
for low_point in low_points:
	basin_points = [low_point]
	for i in range(len(data) * len(data[0])):
		if i >= len(basin_points):
			basin_sizes.append(len(basin_points))
			break
		row = basin_points[i][0]
		col = basin_points[i][1]
		if row != 0 and data[row-1][col] < "9" and data[row-1][col] > data[row][col]:
			if [row-1, col] not in basin_points:
				basin_points.append([row-1, col])
		if row != len(data) - 1 and data[row+1][col] < "9" and data[row+1][col] > data[row][col]:
			if [row+1, col] not in basin_points:
				basin_points.append([row+1, col])
		if col != 0 and data[row][col - 1] < "9" and data[row][col - 1] > data[row][col]:
			if [row, col-1] not in basin_points:
				basin_points.append([row, col-1])
		if col != len(data[0]) - 1 and data[row][col + 1] < "9" and data[row][col + 1] > data[row][col]:
			if [row, col+1] not in basin_points:
				basin_points.append([row, col+1])
		i += 1

basin_sizes.sort(reverse=True)
print(basin_sizes)
print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])
			
			
			
			
#print(data)