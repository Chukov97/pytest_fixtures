from pydantic_settings import BaseSettings


class Config(BaseSettings):

    base_url: str = 'https://github.com'
    driver_name: str = 'chrome'
    load_strategy: str = 'eager'
    window_width_desktop_1: int = 1920
    window_height_desktop_1: int = 1080
    window_width_desktop_2: int = 1700
    window_height_desktop_2: int = 900
    window_width_mobile_1: int = 400
    window_height_mobile_1: int = 870
    window_width_mobile_2: int = 480
    window_height_mobile_2: int = 930
    timeout: float = 4.0


config = Config()
