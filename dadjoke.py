introduction='''hi 
                welcome to this game.
                i am  random  dad joke generater.'''
print(introduction)
print('''let's do this
         but first enter a number
         between 1-3.''')
number=int(input())
if number >=1 and number <=3:
  print("here's your joke..")
  if number == 1 :
      print(''' Why don't eggs tell jokes? 
            Because they might crack up!''')
  else:
      print('''Why did the bicycle fall over? 
            Because it was two-tired!''')
  if number ==2 :
      print('''Why don't scientists trust atoms?
            Because they make up everything!!!!''')
  else:
      print(''' How do you make a tissue dance? 
                 You put a little boogie in it!''')
  if number ==3:
            print('''Why don't melons ever get married?
             Because they can't elope!''')
  else:
      print('''Why don't skeletons fight each other? 
      They don't have the guts!''')
else:
    print("oops , you entered number is not between 1-3..")
    print("see you next time..........")


         
    
