introduction = '''Welcome to the "QR Code Generator" App.
                In this app, you'll enter your website
                or any other URL, and then we'll generate
                a QR Code for the given URL. Then a browser 
                will open, and you will see a QR Code.'''
print(introduction)
import pyqrcode
import random
import webbrowser
from pyqrcode import QRCode
URL = input("Enter your URL here: https://")
colours = ["#ff1493", "#f5cfca", "#ff9a00", "#3ac9b7"]
color = random.choice(colours)
colour_1 = "#cc0443"
colour_2 = "#4e48f8"
colour_3 = "#00ff00"
colour_4 = "#fffc00"
colour_5 = "#133337"
size = input("Enter a number for the size of your QR code (must be between 5-10): ")
color_choice = input('''What color do you want 
                   for your QR Code? Write the 
                   number from the given options:
                   1-red
                   2-blue
                   3-green 
                   4-yellow
                   5-black
                   6-computer choice
                   //:''')
if color_choice == "1":
    module_color = colour_1
elif color_choice == "2":
    module_color = colour_2
elif color_choice == "3":
    module_color = colour_3
elif color_choice == "4":
    module_color = colour_4
elif color_choice == "5":
    module_color = colour_5
elif color_choice == "6":
    module_color = color
else:
    module_color = color 
QRcode = pyqrcode.create(URL)
QRcode.svg("QRcode.svg", scale=size, module_color=module_color, title="QR Code")
webbrowser.open("QRcode.svg")
