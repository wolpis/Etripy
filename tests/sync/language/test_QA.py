import pytest
from etripy.sync import QAClient, WikiType

text = "가스파초는 어느 나라의 음식인가요?"
mrc_p = "루트비히 판 베토벤(독일어: Ludwig van Beethoven, 문화어: 루드위히 판 베토벤, 1770년 12월 17일 ~ 1827년 3월 26일)은 독일의 서양 고전 음악 작곡가이다. 독일의 본에서 태어났으며, 성인이 된 이후 거의 오스트리아 빈에서 살았다. 감기와 폐렴으로 인한 합병증으로 투병하다가 57세로 생을 마친 그는 고전주의와 낭만주의의 전환기에 활동한 주요 음악가이며, 작곡가로 널리 존경받고 있다. 음악의 성인(聖人) 또는 악성(樂聖)이라는 별칭으로 부르기도 한다. 가장 잘 알려진 작품 가운데에는 〈교향곡 5번〉, 〈교향곡 6번〉, 〈교향곡 9번〉, 〈비창 소나타〉, 〈월광 소나타〉 등이 있다."
mrc_q = "베토벤이 누구야?"
wiki_q = "김구가 누구야?"
legal_q = "대법원장의 임기는 몇년인가?"
doc_key = "2c1b1020-4022-4110-933d-8ef8a77ff64c_8B3E507A7F0001017810168D008A18DA"  # 교통안전법_시행규칙.hwp
doc_q = "교통안전법 시행규칙의 목적은?"


# 질문 분석
def test_analysis(qa: QAClient):
    r = qa.qanal(text=text)
    assert r.data


# 기계 독해
def test_mrc(qa: QAClient):
    r = qa.mrcservlet(question=mrc_q, passage=mrc_p)
    assert r.data


# 위키백과
def test_wiki(qa: QAClient):
    r = qa.wiki(type=WikiType.hybridqa, question=wiki_q)
    assert r.data


# 법률
def test_legal(qa: QAClient):
    r = qa.legal(question=legal_q)
    assert r.data


# 행정문서
def test_docfile(qa: QAClient):
    r = qa.doc(doc_key=doc_key, question=doc_q)
    assert r.data
