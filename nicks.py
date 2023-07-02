introduction='''Welcome to the 'Random Nickname Generator'!

    In this app, you'll enter your first and last
    name, and then we'll choose a random nickname
    for you.
    would you like to play this game???
    (y/n:)'''
print(introduction)
answer1=input()
if answer1 == "y" or answer1 == "yes":
    

    import random
    first=input("what is your first name??")
    last=input("what is your last name???")
    print("ok , here's your nickname")
    nick="Tex" , "Rex" , "trotter" , "ace" ,"duke" , "gizmo"
    print(first,random.sample(nick , 1) ,last)
    print("did you like your name (y/n) :")
    answer2=input()
    if answer2 =="y" or answer2 == "yes":
        print("thanks.")
        print("how was the game quality???")
        answer3=input()
        print("thanks for your feedback.")
        print("good bye")
        print("see you next time...........")
    else:
        print(" no problem , try again.")
else:
    print("ok , no problem")
    print("good bye")
    print("see you next time...........")
