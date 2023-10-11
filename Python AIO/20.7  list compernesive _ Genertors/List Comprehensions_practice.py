'''You are given three integers x,y and z representing the dimensions of a cuboid along with an integer . 

Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the 
sum of  i + j + k is not equal to n. Here, i<x;j<y;z<k. 

Please use list comprehensions rather than multiple loops, as a learning exercise.'''



x = int(input("x :"))
y = int(input("y :"))
z = int(input("z :"))
n = int(input("n :"))

##cuboid = []
##for i in range(0,x+1):
##        for j in range(0,y+1):
##                for k in range(0,z+1):
##                        if i+j+k != n:
##                                cuboid.append([i, j, k])
##
##print(cuboid)

#####below code is same but list comp..

cuboid = [[i,j,k]for i in range (0,x+1) for j in range (0,y+1)  for k in range(0,z+1) if i+j+k != n]
print(cuboid)
