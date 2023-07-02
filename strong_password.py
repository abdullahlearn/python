import random
password_lenght = int(input("enter your password desired length:"))
if password_lenght >=6 and password_lenght <=20:
    print(" ok , here's your  password.")
    alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits ='0123456789'
    sepcials = '¬!"£$%^&*()_+<>@:#'
  
    printing_password4=random.sample(alphabets+digits+sepcials,   password_lenght )
    printing_password=printing_password4
    print(''.join(printing_password))

    question=input("did you like this password??? (y/n): ")
    if (question == "y" or "yes"):
        print("thanks")
    else:
        print("no problem , try again")

    print("how was the game quality???: ")
    answer=input()
    print("thanks for your feedback..")
    print("good bye")
    print("see you next time.............")
else:
    print("oops, password lenght not supported. It must be between 6 - 20 character lenght")