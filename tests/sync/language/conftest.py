import pytest

from etripy import sync

access_key = "2c1b1020-4022-4110-933d-8ef8a77ff64c"  # 엑세스 키


@pytest.fixture
def analysis():
    return sync.AnalysisClient(access_key=access_key)


@pytest.fixture
def qa():
    return sync.QAClient(access_key=access_key)
