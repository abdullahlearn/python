introduction = '''Welcome to "The Mail Id" App.
                 In this app you'll give us 
                 your any email id  
                 and then we'll print it again
                 but in hidden form.'''
print(introduction)
# Step 1 - Get input of email id or directly provide example email
Id = "abdullahmuhammad.one@gmail.com"
print(Id)
# Step 2 - Separate user name part from email address
username, domain= Id.split('@')
print("this is user name part " + username)
print("this is domain  part " + domain)
# Step 3 - Find length of the user name
username_length = len(username)
print("this is the leght of user name: ",  username_length)
# Step 4 - Replace * sign with all characters of the user name except for the first and the last one
hidden_username = username[0] + "*" * (username_length - 2) + username[-1]
hidden_id = hidden_username + '@' + domain
print(f"Your hidden ID: {hidden_id}")
print("see you next time.......................")
