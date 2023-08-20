introduction='''i am an "even-odd number generator"
                in this app, you'll enter a number
                and then a quick response will be
                generated from your entered number.
                '''
print(introduction)
print("let's do this .")
number=int(input("enter a number:"))
if number % 2 == 0:
        print(number , ": is an even")
else:
   print(number , ": is an odd number")
   print("see you next time.....")