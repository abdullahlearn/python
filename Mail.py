introduction = '''Welcome to "The Mail Id" App.
                 In this app you'll give us 
                 your any email id  
                 and then we'll print it again
                 but in hidden form.'''
print(introduction)
Id = input("enter your email adress:")
username, domain= Id.split('@')
print("this is user name part " + username)
print("this is domain  part " + domain)
username_length = len(username)
print("this is the leght of user name: ",  username_length)
hidden_username = username[0] + "*" * (username_length - 2) + username[-1]
hidden_id = hidden_username + '@' + domain
print(f"Your hidden ID: {hidden_id}")
print("see you next time.......................")
