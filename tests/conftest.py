# This file contains PyTest fixtures used across the test suite.

import json

import httpx
import pytest

from lib.config import config


@pytest.fixture
def test_assets_payloads():
    """This builds the test payloads JSON file"""
    file_contents = config.test_assets_payloads_json_file.read_text(encoding="utf-8")
    yield json.loads(file_contents)

@pytest.fixture
def test_response():
    """This builds the test response JSON file"""
    file_contents = config.test_response_path.read_text(encoding="utf-8")
    yield json.loads(file_contents)

def raise_on_4xx_5xx(response):
    """This function raises an exception if the response status code is 4xx or 5xx

    :param response: HTTPX Response object
    """
    response.raise_for_status()

@pytest.fixture
def httpx_client():
    """This builds the HTTPX Client"""
    # Create a low-level API client to make requests to the API
    client = httpx.Client(
        base_url=config.base_url,
        timeout=30,
        event_hooks={'response': [raise_on_4xx_5xx]}
    )
    yield client

    # Close the client connection after the tests are done
    client.close()
