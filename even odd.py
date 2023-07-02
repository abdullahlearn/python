introduction='''i am an "even-odd number generator"
                in this app, you'll enter a number
                and then a quick response will be
                generated from your entered number.
                would you like to play this game???
                (y/n)'''
print(introduction)
answer=input()
if answer == "y" or answer =="yes":
   print("ok , let's do this .")
   number=int(input("enter a number:"))
   if number % 2 == 0:
        print(number , ": is an even")
   else:
    print(number , ": is an odd number")
    print("how was the game quality???")
   answer2=input()
   print("thanks for your feedback.")
   print("goodbye")
   print("see you next time.....")
else:
   print("no problem")
   print("goodbye")
   print("see you next time.....")


