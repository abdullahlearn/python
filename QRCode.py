introduction='''Welcome to the "QR Code Generater" App.
                In this app you'll enter your website
                or any other URL and then we'll generate
                a QR Code for the given URL , But you can't
                see the QR Code in the terminal . you will
                see  a file in file explorer of QRcode.svg
                you have to open it and thenyou will see a
                QR code in your opened browser.   '''
print(introduction)
import pyqrcode
from pyqrcode import QRCode
URL=input("Enter your URL  here:https://")
QRcode=pyqrcode.create(URL)
QRcode.svg("QRcode.svg",scale =5,module_color= '#00ff00' ,title = "My Code MA")