class KickDownloaderError(Exception):
    """General error"""


class SourceURLNotFound(KickDownloaderError):
    """Source URL could not be found"""
