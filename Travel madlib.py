welcome_message = """Welcome to the 'Mad Libs' app!
                     In this app, you'll respond to the prompts
                     with the correct type of word. A Mad Lib will
                     then be generated from your responses."""

Game_Introduction = """This Madlib will compile and describe your travelling interests 
                       and different acrivities you would love to participate in!!
                       Answer the following questions and a madlib will be generated 
                       from your responses!! Good Luck!"""
print(Game_Introduction)
place = input("Enter your dream travel destination : ")
days = input("Enter the number of days you want to spend: ")
Interests = input("Enter an activity you would like to do ")
Interest_2 = input("Enter another activity you would like to do ")
vehicle = input("Which vehicle would you like to travel in? ")
if vehicle[0] in ("a", "e", "i", "o", "u", "A" , "E" ,"I" , "O" , "U"):
        vehicle = " an " + vehicle
else:
        vehicle = "  a " + vehicle
mad_lib = f"""
    I love to travel, Next year I will visit {place}, Hopefully
    I  will travel through{vehicle}. I want my trip to be planned 
    for atleast {days} days .I would really appreciate the presence of
    {Interests} and {Interest_2} oppurtunities.
    """
print("Here's your Mad Lib!")
print(mad_lib)
print("see you next time ..........................")
