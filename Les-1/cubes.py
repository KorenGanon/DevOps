from time import sleep
from random import randint

print("Welcome to our cubes game\n Turn is 3ILS\n")
cash=int(input("How much cash you have?\n"))
turn = (cash//3)
print("Truns = " + str(turn)+ "\n")
prize=0
for i in range(turn):
    print("Round Number "+str(i+1)+"\n-------------")
    cube1 = randint(1,6)
    cube2 = randint(1,6)
    sleep(3)
    print("Cube 1 ="+str(cube1) + "\n Cube 2 is = " + str(cube2)+ "\n")
    if cube1 == cube2:
        if (cube2 == 6):
            prize = prize + 1000
        else:
            prize = prize + 100
    elif(cube1 == 1):
        prize = prize +20
    elif(cube2 == 2):
        prize = prize +40
print("Prize = " + str(prize))



