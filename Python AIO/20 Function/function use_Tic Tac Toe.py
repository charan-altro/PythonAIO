game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board():
	print("   A  B  C")
	for count, row in enumerate(game):
		print(count, row)

game_board()		

x = game_board
game[0][1] = 1 # game move

x()



'''
   A  B  C
0 [0, 0, 0]
1 [0, 0, 0]
2 [0, 0, 0]
   A  B  C
0 [0, 1, 0]
1 [0, 0, 0]
2 [0, 0, 0]
'''