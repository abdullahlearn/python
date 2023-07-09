intro = '''Welcome to the 'Rock Paper Scissors' app!
          In this app, you will choose one of the 
          options: rock, paper, or scissors.
          The computer will randomly generate its choice 
          as well, and we will determine the winner 
          or if it's a tie.
          Would you like to play this game?
          (y/n):'''

print(intro)
answer = input()

if answer.lower() == "y" or answer.lower() == "yes":
    print("Okay, let's do this!")
    rounds=int(input("How many rounds would you like to play???"))
    import random

    def play():
        word = input("Enter your choice here: ")
        rps = ("rock", "paper", "scissors")
        computer = random.choice(rps)
        print("Computer's choice:", computer)
        
        if word == computer:
            print("It's a tie!")
        elif (word == "rock" and computer == "scissors") or (word == "paper" and computer == "rock") or (word == "scissors" and computer == "paper"):
            print("You won!")
            return True
        else:
            print("You lost!")
            return False

    rounds_won = 0
    total_rounds = rounds
    

    for _ in range(total_rounds):
        if play():
            rounds_won += 1
        print("---------------")

    print("Total rounds won:", rounds_won)
    print("See you next time...")
else:
    print("No problem. See you next time...")
