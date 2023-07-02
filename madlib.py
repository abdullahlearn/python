message='''hi bro 
        Would you like to play a game with chatbot?
        write your answer in 'yes' or 'no' (y/n):'''
print(message)
a=input()
if a =='yes' or a == "y":
    print("Ok,Let's do this.")
    disclaimer=  '''this game is owned by Microsoft.
                So don't worry .
               In this game the chatbot  will 
               ask some questions and then it will
               generate a madlib from your response
               '''

    print(disclaimer)  

    character=input("enter your favourite character:")
    place=input("enter your favourite place:")
    place_2=input("enter another place:")
    place_3=input("enter another place: ")
    school=input("enter a school name:")
    year=input("enter an year:")

    madlib=f'''
        my favourite character is {character}.
         he/she was born in {place} .after completing
         his schooling in {place_2},he/she went to
         {place_3}.he/she decided to do something in that
         place. he/she decided to open a school name
         {school}.he/she died in {year}

           '''


    print(madlib)
    print("see you next time........")
else:
    print("oK,no problem")
    print("see you next time........")

