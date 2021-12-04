# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cfabian <cfabian@student.42wolfsburg.de>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/12/04 09:04:33 by cfabian           #+#    #+#              #
#    Updated: 2021/12/04 10:41:24 by cfabian          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

boards = [[]]
values = []
with open('input.txt') as input:
	line = input.readline()
	values = line.strip('\n').split(',')
	line = input.readline()
	i = 0
	while line != "":
		while line != '\n' and line != "":
			boards[i].append(list(filter(None,line.strip('\n').split(' '))))
			line = input.readline()
		if line == '\n':
			boards.append([])
			i += 1
		line = input.readline()
	#print(boards)
	#print(values)


def winner(boards):
	winners = []
	for board in boards:
		for row in board:
			counter = 0
			for num in row:
				if isinstance(num, int):
					counter += 1
			if counter == 5:
				winners.append(board)
		for col in range(5):
			counter = 0
			for row in board:
				if isinstance(row[col], int):
					counter += 1
			if counter == 5:
				winners.append(board)
	if winners == []:
		return(0)
	return (winners)			
			
		

'''for val in values:
	for i in range(len(boards)):
		for j in range(len(boards[i])):
			boards[i][j] = [int(num) if num == val else num for num in boards[i][j]]
	winning_board = winner(boards)
	if winning_board != 0:
		last_value = val
		break
print(winning_board)
score = 0			
for row in winning_board:
	for num in row:
		if isinstance(num, str):
			score += int(num)
print(f"final score is {score} * {int(last_value)} = {score * int(last_value)}")'''
	
#Part B
for val in values:
	for i in range(len(boards)):
		for j in range(len(boards[i])):
			boards[i][j] = [int(num) if num == val else num for num in boards[i][j]]
	winning_boards = winner(boards)
	if winning_boards != 0:
		print(len(boards))
		for win in winning_boards:
			try:
				boards.remove(win)
			except ValueError:
				print(win)
		#print(winning_boards)
		print(len(boards))		
	if len(boards) == 1:
		print(winning_boards)
		last_value=val
		break
		
print(boards)
score = 0			
for row in winning_boards[0]:
	for num in row:
		if isinstance(num, str):
			score += int(num)
print(f"final score is {score} * {int(last_value)} = {score * int(last_value)}")	
		
		

