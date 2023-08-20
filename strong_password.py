intro='''Welcome to the 'Strong Password Generator' App.
         In this app you'll enter your desired password length
         and then we'll print a strong password for you.'''
import random
password_lenght = int(input("enter your password desired length:"))
if password_lenght >=6 and password_lenght <=20:
    print(" ok , here's your  password.")
    alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits ='0123456789'
    specials = '¬!"£$%^&*()_+<>@:#'
    printing_password2=random.sample(alphabets+digits+specials,   password_lenght )
    printing_password=printing_password2
    print(''.join(printing_password))
    print("see you next time.............")
else:
    print("oops, password lenght not supported. It must be between 6 - 20 character lenght")