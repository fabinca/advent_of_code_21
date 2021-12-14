# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/14 10:28:16 by cfabian           #+#    #+#              #
#    Updated: 2021/12/14 11:43:03 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

with open("input.txt") as f:
	data = f.read().splitlines()

polymer = ""
rules = {}

for line in data:
	if " -> " in line:
		rules[line.split(" -> ")[0]] = line.split(" -> ")[1]
	elif line != "":
		polymer = line

pairs = dict.fromkeys(rules, 0)

i = 1
while i < len(polymer):
	pair = polymer[i-1] + polymer[i]
	pairs[pair] += 1
	i += 1

#print(pairs)

for step in range(40):
	pairs_old = {key:value for (key,value) in pairs.items() if value != 0}
	pairs = dict.fromkeys(rules, 0)
	for key in pairs_old:
		insert_let = rules[key]
		new_pair1 = key[0] + insert_let
		new_pair2 = insert_let + key[1]
		#print(new_pair1, new_pair2, pairs_old[key])
		for new_pair in [new_pair1, new_pair2]:
			pairs[new_pair] += pairs_old[key]
	#print(pairs)

unique_letters = {letter:0 for letter in set(rules.values())}


unique_letters[polymer[0]] += 1
unique_letters[polymer[-1]] += 1
#print(unique_letters)

for key in pairs:
	#print(f"{unique_letters[key[0]]} += {pairs[key]}")
	unique_letters[key[0]] += pairs[key]
	unique_letters[key[1]] += pairs[key]

max = max(unique_letters.values())//2
min = min(unique_letters.values())//2
	
print(min, max)
print(max-min)
	
		

	
	





'''for step in range(10):
	print(step)
	i = 1
	while i < len(polymer):
		pair = polymer[i - 1] + polymer[i]
		for rule in rules:
			if rule[0] == pair:
				polymer = polymer[:i] + rule[1] + polymer[i:]
				i += 1
				break
		i += 1

letters = set(polymer)
print(letters)
min = polymer.count(polymer[0])
max = polymer.count(polymer[0])
for letter in letters: 
	count = polymer.count(letter)
	if count > max:
		max = count
	if count < min:
		min = count'''

#print(f"min: {min}, max = {max}, max-min= {max-min}")
				
