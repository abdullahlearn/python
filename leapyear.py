introduction='''Welcome to the "Leapyear Guesser"
               In this app, you'll enter  an year ,
                 and then we'll response that it is
                 an leapyear or not.
                would you like to play this game???
                 (y/n) :'''
print(introduction)
answer=input()
if answer =="y" or answer =="yes":
    print("ok , let's do this")
    year=int(input("enter an year :"))
    if year % 4 ==0:
        print(year , ":is an leapyear.")
    else:
        print(year , ":is not an leapyear.")
    print("how was the game quality???")
    feedback=input()
    print("thanks for your feedback.")
    print("good bye")
    print("see you next time.")
else:
    print("no problem")    
    print("good bye")
    print("see you next time.")