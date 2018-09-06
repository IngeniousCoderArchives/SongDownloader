import os
import youtube_dl
os.system("setup.bat")
playlist = input("Paste the Youtube Playlist URL Here.")
track = 1
print("""THIS TOOL WILL ATTEMPT TO DOWNLOAD THE FIRST 1000 SONGS IN THE QUEUE.\n
         PLEASE DO NOT INTERRUPT THE TOOL.
         YOU MAY CLOSE THE TOOL WHEN IT DISPLAYS "DONE!".
         ALL DOWNLOADED SONGS WILL BE IN THE SAME DIRECTORY THIS FILE IS IN.
         TO EXTRACT THEM, FILTER BY MP3.""")

for x in range(1000):
  file = open("Downloader.bat","w")
  file.write("youtube-dl -x --playlist-start {} --audio-format mp3 --playlist-end {} {}".format(str(track),str(track),playlist))
  file.close
  os.system("Downloader.bat")
  track = track + 1

print("DONE! You may now close this window.")
