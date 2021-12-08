# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/08 09:28:22 by cfabian           #+#    #+#              #
#    Updated: 2021/12/08 10:48:01 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


with open("input.txt") as file:
	data = file.read().splitlines()
input = []
output = []
for line in data:
	new = ["".join(sorted(num)) for num in line.split(" | ")[0].split(" ")]		
	input.append(new)
	new = ["".join(sorted(num)) for num in line.split(" | ")[1].split(" ")]	
	output.append(new)
	
#print(input)
#part A
# 1: 2 digits
# 4: 4 digits
# 7: 3 digits
# 8: 7 digits

solution = 0 #count 1,4,7,8 in ouput
for line in output:
	for num in line:
		if len(num) in [2,4,3,7]:
			solution += 1
#print(solution)

#part B
wiring = []
solution = []
l = 0
for line in input:
	wiring.append(["" for _ in range(10)])
	for num in line: 
		if len(num) == 2:
			wiring[l][1] = num
		elif len(num) == 4:
			wiring[l][4] = num
		elif len(num) == 3:
			wiring[l][7] = num
		elif len(num) == 7:
			wiring[l][8] = num
	for num in line:
		if len(num) == 6:
			if wiring[l][4][0] in num and wiring[l][4][1] in num and wiring[l][4][2] in num and wiring[l][4][3] in num:
				wiring[l][9] = num
			elif wiring[l][1][0] not in num or wiring[l][1][1] not in num:
				wiring[l][6] = num
			else:
				wiring[l][0] = num
	for num in line:
		if len(num) == 5 and wiring[l][1][0] in num and wiring[l][1][1] in num:
			wiring[l][3] = num
			break
	for num in line:
		if len(num) == 5:
			for letter in num:
				if letter not in wiring[l][3]:
					if letter not in wiring[l][4]:
						wiring[l][2] = num
					else:
						wiring[l][5] = num
	solution.append("")		
	for x in output[l]: 
		for num in wiring[l]:
			if len(num) == len(x):
				if num == x:
					print(x,num)
					solution[l] += str(wiring[l].index(num))
	l += 1
	
print(solution)
sol = 0
for num in solution:
	sol += int(num)
print(sol)