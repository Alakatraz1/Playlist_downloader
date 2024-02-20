# YouTube Playlist Downloader

This Python script enables users to download all videos from a YouTube playlist using the Pytube library. It's particularly useful for archiving or offline viewing purposes. 

Google Colab Notebook:
You can try out the script in Google Colab by [clicking here](https://colab.research.google.com/drive/1ZrtPaH00PyVvKFR2Bd77HZmbXaSMhun7).


## Prerequisites

Before using this script, ensure you have the following installed:
- Python 3.x
- Pytube library
- Google Colab (if running the code in a Colab environment)

## Usage

1. **Clone the Repository:** Clone this repository to your local machine or download the script directly.

    ```
    git clone https://github.com/Alakatraz1/Playlist_downloader.git
    ```

2. **Install Dependencies:** Install the required dependencies by running:

    ```
    pip install pytube google-colab
    ```

3. **Run the Script:**
    - Open the script in a Python IDE or text editor.
    - Input the URL of the YouTube playlist when prompted.
    - Define the location where you want to save the downloaded videos.
    - Execute the script.

Upon execution, the script will prompt you to enter the URL of the YouTube playlist you want to download. After providing the URL, it will start downloading the videos one by one into the specified location.

## How It Works

1. **Mount Google Drive:** This step mounts Google Drive to the Colab environment to facilitate saving the downloaded videos directly to Drive.

2. **Load Playlist:** The script uses Pytube's `Playlist` class to load the playlist from the provided URL.

3. **Create Save Location:** It creates the specified save location directory if it doesn't exist already.

4. **Download Videos:** For each video in the playlist, it selects the highest resolution stream available and downloads it to the specified save location.

5. **Completion Message:** Once all videos are downloaded, it prints a completion message.

## Error Handling

The script includes basic error handling to catch exceptions that may occur during the download process and prints out corresponding error messages.

## Note

- This script is designed for educational purposes and personal use only. Respect copyright laws and terms of service of YouTube when downloading videos.

Feel free to contribute to this project by submitting pull requests or opening issues for suggestions and improvements.

---
*Disclaimer: This script is not affiliated with or endorsed by YouTube.*
