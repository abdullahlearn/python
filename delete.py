introduction='''Welcome to 'The Deleting App' .
                In this app you'll enter  the path
                of your file or anything that you want 
                to delete and then we'll delete it.........'''
print(introduction)
disclaimer='''don't delete your personal or useful files 
                and something else because once we delete it 
                it cannot come back.SO BE ALERT!!!'''
print(disclaimer)
import os
file_path =input('''Enter the path of the file or whatever you want to delete:''')
try:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    else:
        print(f"File {file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
  