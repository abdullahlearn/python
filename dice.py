introduction='''Welcome to the "Dice Roller" app!
            In this app, we will generate two numbers from the dice.
              You can use these numbers in board games or for any other purpose.
                Are you interested in playing this game?
            Please enter 'y' for yes or 'n' for no:'''
print(introduction)
answer=input()
if answer == "y" or answer=="yes":
    print("ok , let's do this.")
    import random
    dice1=[ 1 , 2 , 3 , 4 , 5 , 6]
    dice2=[1 , 2 , 3 , 4 , 5 , 6]
    print(random.sample(dice1, 1))
    print(random.sample(dice2, 1))
    question=input("where you will use these numbers???")
    print('''ok
    see you next time.......''')
else:
    print("ok , no problem.")
    print("see you next time.........")
