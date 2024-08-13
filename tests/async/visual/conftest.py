import pytest
from etripy import client

access_key = ""  # 엑세스 키


@pytest.fixture
def image():
    return client.ImageClient(access_key=access_key)


@pytest.fixture
def video():
    return client.VideoClient(access_key=access_key)
