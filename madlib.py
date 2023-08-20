message='''hi bro 
        Welcome to the 'Madlid Generator App' 
        In this app we'll  ask some questions 
        from you and then we'll generate a madlib
        from your response.'''
print(message)
print("Let's do this.")
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
         {school}.he/she died in {year}'''
print(madlib)
print("see you next time........")
