import pytest
from etripy import client

access_key = "2c1b1020-4022-4110-933d-8ef8a77ff64c"  # 엑세스 키


@pytest.fixture
def analysis():
    return client.AnalysisClient(access_key=access_key)


@pytest.fixture
def qa():
    return client.QAClient(access_key=access_key)
