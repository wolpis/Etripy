import pytest
from etripy import sync

access_key = ""  # 엑세스 키


@pytest.fixture
def analysis():
    return sync.AnalysisClient(access_key=access_key)


@pytest.fixture
def qa():
    return sync.QAClient(access_key=access_key)
