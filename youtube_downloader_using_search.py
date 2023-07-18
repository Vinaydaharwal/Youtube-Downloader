# one download per execution

from pytube import Search, YouTube
import os
import pandas as pd
from tabulate import tabulate

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Downloaded: {bytes_downloaded} / {total_size} bytes ({percentage:.2f}%)")

path = os.getcwd()
print("Current folder's path is:", path)

try:
    if input("Do you want to change the path (y/n): ") == "y":  # You can just skip (press enter) it to keep the path
        path = input("Enter the path: ")
        print("Changed path is:", path)
        print(" ")
except:
    pass

link = Search(input("Enter the YouTube search parameter: ")).results[0].watch_url
yt = YouTube(link, on_progress_callback=on_progress)
title = yt.title
print("Title of the YouTube video:", title)

dic = {
    "Index": [i for i in range(len(yt.streams))],
    "Resolution": [i.resolution for i in yt.streams],
    "Audio Quality": [i.abr for i in yt.streams],
    "Type": [i.type for i in yt.streams],
    'Format': [i.subtype for i in yt.streams],
    "Includes Audio": [i.includes_audio_track for i in yt.streams],
    "Includes Video": [i.includes_video_track for i in yt.streams],
    "Filesize (MB)": [i.filesize_mb for i in yt.streams],
}

df = pd.DataFrame(dic)
df = df.set_index('Index')
print()
table = tabulate(df, headers='keys', tablefmt='fancy_grid')
print(table)
print()

index = int(input("Enter the 'Index' for the format of the video (0-" + str(len(df) - 1) + "): "))
print("\nYou Entered For:")

row_df = pd.DataFrame(df.iloc[index]).transpose()
table = tabulate(row_df, headers='keys', tablefmt='fancy_grid')
print(table)

stream = yt.streams[index]
filename = stream.default_filename
extension = "." + stream.subtype
print("Filename:", filename)
print()

try:
    stream.download(output_path=path)
    print("Download completed  :) ")
    print()
    print("You can find it on:", os.path.join(path, filename))
    print()
    x = input("Do you want to open the file (y/n): ")  # You can just skip (press enter) to skip it (open file)
    try:
        if x == "y":
            os.startfile(os.path.join(path, filename))
    except:
        print("File is downloaded but unable to open")
except:
    print("Download failed : ")
