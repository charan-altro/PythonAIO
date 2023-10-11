game = "I want to play a game"

def game_board():
    game = "A game"

game_board()
print(game)
#I want to play a game

'''Surprise, Python strings are immutable. Oops. 
Hope you knew that! If you were to quiz Python developers, 
I suspect a staggering number of the would not be 
able to confidentally answer if strings are mutable or not. 
So what do you do if you want to still use a function? Well, 
you can re-define'''


game = "I want to play a game"
print(id(game))

def game_board():
    game = "A game"
    print(id(game))
    return game

game = game_board()
print(game)
print(id(game))

'''
34252320
34250608
A game
34250608'''



game = [1, 2, 3]
print(id(game))


def game_board():
    game[1] = 99
    print(id(game))
    return game


game = game_board()
print(game)
print(id(game))

'''
33640904
33640904
[1, 99, 3]
33640904
'''