from .exceptions import *

import json
import os

from selenium.webdriver import Firefox, FirefoxOptions


class KickDownloader:
    API_BASE = "https://kick.com/api/v1/video/"

    def __init__(
        self,
        options: FirefoxOptions = FirefoxOptions(),
        headless: bool = True,
        ffmpeg_path: str = "",
    ) -> None:
        self.ffmpeg_path = ffmpeg_path

        if headless:
            options.headless = True

        self.driver = Firefox(options)

    @staticmethod
    def _extract_video_id(url: str) -> str:
        # https://kick.com/video/98f2e1d2-6eb9-4f68-bc59-de830c7ff3ef
        # -> 98f2e1d2-6eb9-4f68-bc59-de830c7ff3ef
        video_id = url.replace("https://kick.com/video/", "")
        return video_id

    def _get_data(self, video_id: str) -> dict:
        url = self.API_BASE + video_id

        self.driver.get(url)
        page_source = self.driver.page_source
        self.driver.quit()

        json_data_start = "<html><head></head><body>"
        json_data_end = "</body></html>"

        start_index = page_source.find(json_data_start) + len(json_data_start)
        end_index = page_source.find(json_data_end)

        json_data = page_source[start_index:end_index]

        parsed_json = json.loads(json_data)

        return parsed_json

    def _get_source_url(self, url: str) -> str:
        video_id = self._extract_video_id(url)
        data = self._get_data(video_id)
        source_url = data.get("source")
        return source_url

    def download(self, url: str, output_path: str) -> None:
        source_url = self._get_source_url(url)

        if not source_url:
            raise SourceURLNotFound("could not find a source url for given broadcast")

        command = "ffmpeg"

        if self.ffmpeg_path:
            command = self.ffmpeg_path

        command += f" -i {source_url} -vcodec copy -acodec copy {output_path}"
        os.system(command)
