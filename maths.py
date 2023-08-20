introduction = '''Welcome to the "Table Generator"
                In this app, you'll enter 
                a number, and then we'll 
                print the table of that number.
                '''
print(introduction)
number = int(input("Enter a number: "))
print("Here's the table for", number, ":")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
print("Thanks for your feedback.")
print("Goodbye!")
print("See you next time...")

