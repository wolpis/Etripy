import pytest
from etripy import client

access_key = ""  # 엑세스 키


@pytest.fixture
def analysis():
    return client.AnalysisClient(access_key=access_key)


@pytest.fixture
def qa():
    return client.QAClient(access_key=access_key)
