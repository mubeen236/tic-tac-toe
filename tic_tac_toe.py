'''
A simple Tic Tac Toe game with 2 players
Author: Madiha Mubeen
Date: May 26, 2018
'''
import random

def display_board(board):
	print(board[0]+'|'+board[1]+'|'+board[2])
	print(board[3]+'|'+board[4]+'|'+board[5])
	print(board[6]+'|'+board[7]+'|'+board[8])

def intro():
	user=''
	while user!='x' and user!='y':
		user=input('Would you like to play as x or y?')
	if user=='x':
		player1,player2='x','y'
	else:
		player1,player2='y','x'
	print('Thank you, Let''s play!')
	return player1,player2

def player_turn():
	result = random.randint(1,2)
	if result == 1:
		return 'player1'
	else:
		return 'player2'

def check_space(board,position):
	if board[position]==' ':
		return True
	else:
		return False

def insert(board,position,player):
	board[position]=player

def win_check(board):
	#straight check
	if board[0]!=' ' and board[0]==board[1] and board[1]==board[2]:
		return True
	elif board[3]!=' ' and board[3]==board[4] and board[4]==board[5]:
		return True
	elif board[6]!=' ' and board[6]==board[7] and board[7]==board[8]:
		return True
	#downwards check
	if board[0]!=' ' and board[0]==board[3] and board[3]==board[6]:
		return True
	elif board[1]!=' ' and board[1]==board[4] and board[4]==board[7]:
		return True
	elif board[2]!=' ' and board[2]==board[5] and board[5]==board[8]:
		return True
	#diag check
	if board[0]!=' ' and board[0]==board[4] and board[4]==board[8]:
		return True
	elif board[2]!=' ' and board[2]==board[4] and board[4]==board[6]:
		return True
	else:
		return False

def tie_check(board):
	for item in board:
		if item==' ':
			return False
	return True

def replay():
	result=''
	while result!='Y' and result!='N':
		result=input('Do you want to play again? Y or N?')
	if result=='Y':
		play_game()
	else:
		return ('Thanks, game ended!')

def play_game():
	myboard=[' ']*10
	display_board(myboard)
	player1,player2=intro()
	turn=player_turn()
	game_on=True
	while game_on:
		while turn=='player1':
			print('Player 1 turn')
			position=int(input('Enter a position between 0-8 where you want to insert: '))
			if position not in range(0,8):
				print(f'You chose position {position} which is not in the range of 0-8, LOST TURN')
				turn='player2'
			if check_space(myboard,position):
				insert(myboard,position,player1)
				display_board(myboard)
			if win_check(myboard):
				print('Player 1 has won, game ended!')
				game_on=False
				break
			if tie_check(myboard):
				print('Game is a tie')
				game_on=False
			turn='player2'

		else: #player 2 turn
			print('Player 2 turn')
			position=int(input('Enter a position between 0-8 where you want to insert: '))
			if position not in range(0,8):
				print(f'You chose position {position} which is not in the range of 0-8, LOST TURN')
				turn='player1'
			if check_space(myboard,position):
				insert(myboard,position,player2)
				display_board(myboard)
			if win_check(myboard):
				print('Player 2 has won, game ended!')
				game_on=False
			if tie_check(myboard):
				print('Game is a tie')
				game_on=False
			turn='player1'
	replay()

if __name__=='__main__':
	play_game()