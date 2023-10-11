game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game_map[row][column] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return game_map

#game = game_board(game, player=1, row=3, column=1)
#IndexError: list index out of range

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except:
        print("A bad thing just happened.")
        return False

game = game_board(game, player=1, row=3, column=1)

#A bad thing just happened.


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Did you attempt to play a row or column outside the range of 0,1 or 2? (IndexError)")
        return False
    except Exception as e:
        print("something went very wrong!",str(e))
        return False


game = game_board(game_board, player=1, row=1, column=1)