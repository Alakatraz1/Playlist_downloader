!pip install pytube
from pytube import Playlist, YouTube  # Importing YouTube object
from google.colab import drive

def download_youtube_playlist(playlist_url, save_location):
    # Mount Google Drive
    drive.mount('/content/drive')

    try:
        # Load playlist
        playlist = Playlist(playlist_url)

        # Loop through each video in the playlist
        for video_url in playlist.video_urls:
            # Download the video
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=save_location)
            print(f"Downloaded: {yt.title}")

        print("Download completed successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Input the URL of the YouTube playlist
playlist_url = input("Enter the URL of the YouTube playlist: ")

# Define the location to save the downloaded videos
save_location = '/content/drive/My Drive/YouTube_Playlist/'

# Call the function to download the playlist
download_youtube_playlist(playlist_url, save_location)
