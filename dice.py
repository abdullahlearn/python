introduction='''Welcome to the "Dice Roller" app!
            In this app, we will generate two numbers from the dice.
              You can use these numbers in board games or for any other purpose.
                '''
print(introduction)
print(" let's do this.")
import random
dice1=[ 1 , 2 , 3 , 4 , 5 , 6]
dice2=[1 , 2 , 3 , 4 , 5 , 6]
print(random.sample(dice1, 1))
print(random.sample(dice2, 1))
question=input("where you will use these numbers???")
print('''ok   ,see you next time.......''')
