introduction='''Welcome to the 'Youtube video downloading app'.
                In this app you'll enter a youtube video URL that
                you want to download in the computer.you'll will 
                give us a path of any folder where you want to 
                 download the video.we will also show you the 
                 title and views '''
print(introduction)
from pytube import YouTube

try:
    url = input("Enter the YouTube URL: ")
       
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)
    

    yd = yt.streams.get_highest_resolution()
    
    path=input('''Enter the path of the folder
                 where you want to download the video: ''')
    yd.download( path)
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))