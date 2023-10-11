game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

game[0][1] = 1 # index 1st list and 2nd index position

print("   A  B  C")

for count, row in enumerate(game):
    print(count, row)




'''
o/p
   A  B  C
0 [0, 1, 0]
1 [0, 0, 0]
2 [0, 0, 0]
'''