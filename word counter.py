introduction='''Welcome to the "Word Counter" app.
             In this app, you'll enter a sentence, 
             and we'll respond with the number of words
               you've typed in your conviction.
                 Would you like to play this game?
                   (y/n):'''
print(introduction)
answer=input()
if answer =="y" or answer =="yes":
    print("ok , let's do this.")
    sentence=input("write your sentence here:")
    count words = len(sentence.split())
    print("Count of Words in the given Sentence:", Count words)
    print("see you next time.......")
else:
    print("ok  , no problem")
    print("see you next time..........")
