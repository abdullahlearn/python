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
size = int(input("Enter a number for the size of your QR code (must be between 5-10): "))
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
colour_choices = {
    "1": "#cc0443",   # red
    "2": "#4e48f8",   # blue
    "3": "#00ff00",   # green
    "4": "#fffc00",   # yellow
    "5": "#133337",   # black
}    

module_color = colour_choices.get(color_choice, color)
QRcode = pyqrcode.create(URL)
QRcode.svg("QRcode.svg", scale=size, module_color=module_color, title="QR Code")
webbrowser.open("QRcode.svg")
