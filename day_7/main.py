0# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/07 09:51:16 by cfabian           #+#    #+#              #
#    Updated: 2021/12/07 09:52:55 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


with open("input.txt") as file:
	data = [int(num) for num in file.readline().strip('/n').split(',')]
data.sort()
arith = sum(data)/len(data)
medi = data[round(len(data)/2 - 1)]

print(round(len(data)/2 - 1))

solution = []
for possib in range(450, 550):
	fuel = 0
	for num in data:
		increase_rate = 1
		while num < possib:
			num += 1
			fuel += increase_rate
			increase_rate += 1
		while num > possib:
			num -= 1
			fuel += increase_rate
			increase_rate += 1
	solution.append(fuel)
	#print(fuel, "goin to", possib)


print(solution)
print(min(solution))