from pytube import YouTube

# prompt the user for a video URL
url = input("Enter YouTube video URL: ")

# create a YouTube object
yt = YouTube(url)

# get the audio stream of the video
audio_stream = yt.streams.filter(only_audio=True).first()

# download the audio stream as an mp3 file
audio_stream.download(output_path="./", filename=yt.title + ".mp3")

print("Download complete.")
