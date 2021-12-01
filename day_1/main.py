# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/01 15:09:23 by cfabian           #+#    #+#              #
#    Updated: 2021/12/01 16:05:09 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from types import SimpleNamespace


data = []
with open("input.txt", 'r') as file:
	data = file.read().splitlines()

data = list(map(int, data))

## part A
i = 0
increase_num = 0
with open("result_A.txt", 'w') as file:
	while i + 1 < len(data):
		if data[i + 1] > data[i]:
			increase_num += 1
		file.write(f"{data[i]}\t\t{data[i+1]}\t\t{increase_num}\n")
		i += 1
print("Part A ", increase_num)

## part B
i = 0
sliding_window = []
while i + 3 < len(data):
	sum = data[i] + data[i+1] + data[i+2]
	sliding_window.append(sum)
	i += 1

i = 0
increase_num = 0
with open("result_B.txt", 'w') as file:
	while i + 1 < len(sliding_window):
		if sliding_window[i + 1] > sliding_window[i]:
			increase_num += 1
		file.write(f"{sliding_window[i]}\t\t{sliding_window[i+1]}\t\t{increase_num}\n")
		i += 1
print("Part B ", increase_num)
	