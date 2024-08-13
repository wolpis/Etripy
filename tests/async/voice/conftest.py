import pytest
from etripy import client

access_key = ""  # 엑세스 키


@pytest.fixture
def voice():
    return client.VoiceClient(access_key=access_key)
