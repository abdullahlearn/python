introduction='''Welcome to the "Maths Questions Generator" app!
                In this app, you will enter your age,
                  and a math question will be generated based on your entered age.
                    Are you interested in playing this game?
                Please enter 'y' for yes or 'n' for no:'''
print(introduction)
answer=input()
if answer=="y" or answer =="yes":
    print("ok , let's do this")
    age=int(input("enter your age:"))
    if age >= 5 and age <= 10:
        print("what is 100+200-150???")
        answer2=input()
        if answer2== "150" :
            print('''good job
            your answer is correct''')   
        else:
            print('''you are absent minded .
            your answer is incorret''')
    elif age >= 10 and age <= 20:
        print("what is 120-65*98+2???")
        answer3=input()
        if answer3 == "1080":
            print('''good job
            your answer is correct''')   
        else:
            print('''you are absent minded .
            your answer is incorret''')
    elif age >=20:
        print("what is 123-45*9divded by 2 +9???")
        answer4=input()
        if answer4=="360":
            print('''good job
            your answer is correct''')   
        else:
            print('''you are absent minded .
            your answer is incorret''')

            print("see you next time.............")
else:
     print("see you next time.............")





        