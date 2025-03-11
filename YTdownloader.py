import pytube

link = input("Enter link : ")

try:
    yt = pytube.YouTube(link)
    print(yt.title, " - Downloading") 
except:
    print("Connection Error!!!")
    exit(1)
    
try:
    vid = yt.streams.get_highest_resolution()
    vid.download("C:/Users/nisan/Desktop/code")
except:
    print("Something went wrong!!")
    exit(1)