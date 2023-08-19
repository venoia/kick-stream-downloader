# kick-stream-downloader
Download Kick streams/vods using Selenium and FFmpeg.

## Example
```python
>>> from kick_downloader.kick import KickDownloader
>>> downloader = KickDownloader()

>>> downloader.download("https://kick.com/video/663f4bc0-766b-42b4-801e-57311cea0b42", "./output.mp4")
```

If you edit the `download` method you can also just print out the source url (a `.m3u8` address) and watch the vod using VLC.

## Setup
Clone the repository
```bash 
git clone git@github.com:venoia/kick-stream-downloader.git
```

Install the required dependencies
```bash
cd kick-stream-downloader
pip install -r "requirements.txt"
``` 

**geckodriver and FFmpeg should also be downloaded and added to PATH.**

If FFmpeg is not added to PATH, you can specify `ffmpeg_path` in the `KickDownloader` class.
```python
downloader = KickDownloader(ffmpeg_path="C:/Users/username/Downloads/ffmpeg.exe")
```

## Donate
BTC: `bc1qntlxs7v76j0zpgkwm62f6z0spsvyezhcmsp0z2`
