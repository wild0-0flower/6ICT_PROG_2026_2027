from random import randint

lijst_2D = [ [randint(0,5), randint(0,5), randint(0,5)],
             [randint(0,5), randint(0,5), randint(0,5)],
             [randint(0,5), randint(0,5), randint(0,5)] ]
lijst_2D[1][0] = 6
lijst_2D[0][2] = 6
lijst_2D[1][1] = lijst_2D[1][1] * -1
lijst_2D[2][2] = lijst_2D[2][2] * -1
print(lijst_2D)