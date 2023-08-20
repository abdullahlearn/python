import random
intro = '''Welcome to the 'Rock Paper Scissors' app!
          In this app, you will choose one of the 
          options: rock, paper, or scissors.
          The computer will randomly generate its choice 
          as well, and we will determine the winner 
          or if it's a tie.'''
print(intro)
print("let's do this!")
rounds = int(input("How many rounds would you like to play? "))
def play():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    rps = ("rock", "paper", "scissors")
    computer_choice = random.choice(rps)
    print("Computer's choice:", computer_choice)
    if user_choice == computer_choice:
            print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You won!")
            return True
    else:
            print("You lost!")
            return False
    rounds_won = 0
    for _ in range(rounds):
       if play():
            rounds_won += 1
    print("---------------")
    print("Total rounds won:", rounds_won)
    print("See you next time...")

