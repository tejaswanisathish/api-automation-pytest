# This file contains test configuration data

from pathlib import Path

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """This class contains the configuration data for the test suite"""
    base_url: str = "https://reqres.in" # This is the base URL for the API
    test_assets_payloads_json_file: Path = Path("test_assets/test_payloads.json") 
    # This contains the contents of the test payloads JSON file
    test_response_path: Path = Path("test_assets/api_responses.json") 
    # This contains the contents of the test response JSON file

config = Config()
