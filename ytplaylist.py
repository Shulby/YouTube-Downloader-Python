from pytube import Playlist, YouTube

# prompt the user for a playlist URL
playlist_url = input("Enter YouTube playlist URL: ")

# create a Playlist object
playlist = Playlist(playlist_url)

# iterate through each video in the playlist
for video_url in playlist.video_urls:
    # create a YouTube object for the video
    yt = YouTube(video_url)

    # get the audio stream of the video
    audio_stream = yt.streams.filter(only_audio=True).first()

    # download the audio stream as an mp3 file
    audio_stream.download(output_path="./", filename=yt.title + ".mp3")

print("Download complete.")
