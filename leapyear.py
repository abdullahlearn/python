introduction='''Welcome to the "Leapyear Guesser"
               In this app, you'll enter  an year ,
                 and then we'll response that it is
                 an leapyear or not.
                '''
print(introduction)
print(" let's do this")
year=int(input("enter an year :"))
if year % 4 ==0:
        print(year , ":is an leapyear.")
else:
        print(year , ":is not an leapyear.")
print("see you next time.")