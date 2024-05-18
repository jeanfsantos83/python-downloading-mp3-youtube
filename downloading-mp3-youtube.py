# pip install pytube #
# pip install moviepy #
from pytube import YouTube
import moviepy.editor as mp
import re
import os

# Enter the video link and the location you want to save the mp3 #
link = input("Enter the link of the video you want to download: ")
path = input("Enter the directory you want to save the video: ")
yt = YouTube(link)

# Download Start #
print("Downloading...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Full download!")

# Convert mp4 to mp3 #
print('Converting file...')
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print('Sucess!')
