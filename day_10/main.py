# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/10 10:06:12 by cfabian           #+#    #+#              #
#    Updated: 2021/12/10 11:00:57 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

with open("input.txt") as file:
	data = file.read().splitlines()

pairs = {
  "(": ")",
  "[": "]",
  "{": "}",
  "<": ">"
}

#part A
error_points = {
	")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

#part B
completion_points = {
	")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

error_score = 0
completion_score = []

for line in data:
	stack = []
	corrupted = False
	for char in line:
		if char in ["(", "{", "[", "<"]:
			stack.append(char)
		else:
			if  len(stack) == 0:
				error_score += error_points[char]
				corrupted = True
				break
			last = stack.pop()
			if pairs[last] != char:
				error_score += error_points[char]
				corrupted = True
				break
	if not corrupted:
		score = 0
		while len(stack) > 0:
			score = score*5
			score += completion_points[pairs[stack.pop()]]
		completion_score.append(score)

print("Error_score= ",error_score)	
completion_score.sort()
print(completion_score)
print(completion_score[len(completion_score)//2])


			
