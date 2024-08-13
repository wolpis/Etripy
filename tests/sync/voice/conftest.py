import pytest
from etripy import sync

access_key = ""  # 엑세스 키


@pytest.fixture
def voice():
    return sync.VoiceClient(access_key=access_key)
