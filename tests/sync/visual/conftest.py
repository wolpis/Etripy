import pytest
from etripy import sync

access_key = ""  # 엑세스 키


@pytest.fixture
def image():
    return sync.ImageClient(access_key=access_key)


@pytest.fixture
def video():
    return sync.VideoClient(access_key=access_key)
