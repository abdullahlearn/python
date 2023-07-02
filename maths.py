introduction='''Welcome to the "Table Generator"
                In this app  you'll enter 
                a number  and  then we'll 
                print the table of that number.
                Would you like to play this game???
                (y/n):'''
print(introduction)
answer=input()
if answer =="y" or answer == "yes":
    print("ok , let's do this")
    number = int(input("Enter a number: "))

    for i in range(1,11):
        result = number * i
        print(f"{number} x {i} = {result}")
    print("how was the game quality???")
    feedback=input()
    print("thanks for your feedback.")
    print("good bye ")
    print("see you next time..........")
else:
    print("no problem")
    print("good bye ")
    print("see you next time..........")

