# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/02 20:47:20 by cfabian           #+#    #+#              #
#    Updated: 2021/12/02 21:21:44 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


with open("input.txt", 'r') as file:
	data = file.read().splitlines()

#print(data)
'''## PArt A
horizontal = 0
depth = 0
for entry in data:
	dir = entry.split(" ")[0]
	steps = int(entry.split(" ")[1])
	if dir == "forward":
		horizontal += steps
	elif dir == "down":
		depth += steps
	elif dir == "up":
		depth -= steps
	else:
		print(f"Error dir= {dir}")

print(f"Final horizontal position = {horizontal},\n Final depth= {depth}, \n multiplied: {horizontal*depth} \n")'''

## PArt B
horizontal = 0
aim = 0
depth = 0
for entry in data:
	dir = entry.split(" ")[0]
	steps = int(entry.split(" ")[1])
	if dir == "forward":
		horizontal += steps
		depth += aim * steps
	elif dir == "down":
		aim += steps
	elif dir == "up":
		aim -= steps
	else:
		print(f"Error dir= {dir}")
	

print(f"Final horizontal position = {horizontal},\n Final depth= {depth}, \n multiplied: {horizontal*depth} \n")
	