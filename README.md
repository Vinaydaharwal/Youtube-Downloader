# YouTube Downloader

This script allows you to download YouTube videos based on a search parameter. It uses the `pytube` library to fetch and download videos from YouTube. You can only download one video per execution of the script.

## Requirements

- Python 3.6+
- `pytube` library
- `pandas` library
- `tabulate` library

## Installation

If you don't have the required libraries installed, you can install them using the following command:

```bash
pip install pytube pandas tabulate
```
## Caution
1. For downloading high-quality videos above 720p, you need to download separate video and audio files and then merge them.
2. It will override the video file if the path and name of the file are the same.
3. The script may not work for videos with age restrictions.
4. It might take some time to fetch the video after displaying the caution message.

## Usage
1. Run the script in a Python environment that has the required libraries installed.

2. The script will prompt you to enter a YouTube search parameter. Based on your input, it will fetch the first video's link from the search results.

3. It will display a table of available video formats, including resolution, audio quality, type, format, and file size.

4. Enter the index number corresponding to the video format you want to download.

5. The script will download the selected video to the default path or the path you provided.

6. If the download is successful, it will display the download location and prompt you to open the file.

7. If you choose to open the file, the script will attempt to open it with the default application.

## Note
If you encounter issues installing pytube, you can search for pytube on GitHub or other platforms, download the ZIP file, and manually extract it to the site-packages directory of your Python environment.

## Error 
If you encounter occasional issues with the Pytube module due to regular expression errors, there are two potential solutions you can try:

1. Wait for a few days before attempting to use the Pytube module again. Sometimes, these errors can be temporary and may get resolved in future updates.
2. To troubleshoot the problem immediately, follow these steps:

First, uninstall the Pytube module using the command:
```bash
pip uninstall pytube
```
Next, reinstall the Pytube module with the latest version using the command:

```bash
pip install pytube
```

## About this file
This is the markdown file created using [readme.so](https://readme.so/) and [ChatGPT](https://chat.openai.com/)
