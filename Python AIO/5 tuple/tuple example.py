programming_languages = "Python", "Java", "C++", "C#"
print(type(programming_languages ))
# <class 'tuple'>
programming_languages = ("Python", "Java", "C++", "C#")
print(type(programming_languages ))
# <class 'tuple'>




game = (0, 0, 0,
        0, 0, 0,
        0, 0, 0,)

print(game)
#(0, 0, 0, 0, 0, 0, 0, 0, 0)
print(type(game))
#<class 'tuple'>

game = ((0, 0, 0),
        (0, 0, 0),
        (0, 0, 0),)

print(game)
for row in game:
    print(row)
