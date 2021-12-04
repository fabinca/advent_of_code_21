# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/03 17:44:52 by cfabian           #+#    #+#              #
#    Updated: 2021/12/03 19:06:11 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from datetime import datetime
start = datetime.now()

with open("input.txt", 'r') as file:
	data = file.read().splitlines()
# idea: bitwise list -> 
bitwise = []

for bit in data[1]:
	if bit == "0" or bit == "1":
		bitwise.append(0)
	else: print(bit)
bitwise_copy = bitwise

##Part A
for entry in data:
	for i in range(len(bitwise)):
		if entry[i] == "0":
			bitwise[i] -= 1
		elif entry[i] == "1":
			bitwise[i] += 1
		elif entry[i] != "\n":
			print("Error:", entry[i])
print(bitwise)
# negative number means 0 most frequent, positive one most frequent

gamma_rate_bin = ""
epsilon_rate_bin = ""
for bit in bitwise:
	if bit > 0:
		gamma_rate_bin += "1"
		epsilon_rate_bin += "0"
	elif bit < 0:
		gamma_rate_bin += "0"
		epsilon_rate_bin += "1"
	else: 
		print("Error", bit)
gamma_int = int(gamma_rate_bin, 2)
epsilon_int = int(epsilon_rate_bin, 2)
print("binary:\t", gamma_rate_bin, epsilon_rate_bin)
print("int:\t", gamma_int, epsilon_int)
print("multiplied:\t", gamma_int*epsilon_int)

##Part B
data_copy = data
#for oxy 
bitwise = [bit * 0 for bit in bitwise]
i = 0
while len(data) > 1 and i < len(bitwise):
	for entry in data:
		if entry[i] == "0":
			bitwise[i] -= 1
		elif entry[i] == "1":
			bitwise[i] += 1
		elif entry[i] != "\n":
			print("Error:", entry[i])
	if bitwise[i] >= 0:
		data = [entry for entry in data if entry[i] == "1"]
	else:
		data = [entry for entry in data if entry[i] == "0"]
	i += 1
print(data)
oxy = int(data[0], 2)

#co2 is basicaly the same except line 83 & 85
bitwise = [bit * 0 for bit in bitwise]
data = data_copy
i = 0
while len(data) > 1 and i < len(bitwise):
	for entry in data:
		if entry[i] == "0":
			bitwise[i] -= 1
		elif entry[i] == "1":
			bitwise[i] += 1
		elif entry[i] != "\n":
			print("Error:", entry[i])
	if bitwise[i] >= 0:
		data = [entry for entry in data if entry[i] == "0"]
	else:
		data = [entry for entry in data if entry[i] == "1"]
	i += 1
co_2 = int(data[0], 2)
print(data)
print(f"oxy: {oxy}, co_2: {co_2}, multiplied: {oxy*co_2}")

end = datetime.now()
print(end-start)