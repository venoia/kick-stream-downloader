from kick_downloader.kick import KickDownloader

from selenium.webdriver import FirefoxOptions


options = FirefoxOptions()
downloader = KickDownloader(options=options, headless=True, ffmpeg_path="")


downloader.download(
    "https://kick.com/video/663f4bc0-766b-42b4-801e-57311cea0b42", "./video.mp4"
)
