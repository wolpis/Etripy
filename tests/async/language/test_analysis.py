import pytest
from etripy.client import AnalysisClient, AnalysisCode

analysis_text = "엑소브레인은 내 몸 바깥에 있는 인공 두뇌라는 뜻으로, 세계 최고인공지능 기술 선도라는 비전을 달성하기 위한 과학기술정보통신부 소프트웨어 분야의 국가 혁신기술 개발형 연구개발 과제이다."
sentences = (
    "성탄 전야 미사를 집전하며 프란치스코 교황이 전한 메시지는 '어린이를 향한 관심'입니다.",
    "프란치스코 교황의 올해 첫 성탄 메시지는 고통받는 어린이를 향한 관심이었습니다.",
)
word_1 = "배"
word_2 = "사과"
NE_text = "노벨 물리학상( - 物理學賞, 스웨덴어: Nobelpriset i fysik, 영어: Nobel Prize in Physics)은 6개 분야의 노벨상 중 하나로, 1년에 한 번 스웨덴 왕립 과학원에 의해 수여된다. 첫 번째 노벨 물리학상은 1901년, 엑스선을 발견한 독일의 빌헬름 콘라트 뢴트겐에게 수여되었다. 이 상은 노벨 재단이 주관하며, 이 상을 수상하는 것은 물리학계에서 최고의 영예로 꼽힌다. 노벨 물리학상은 알프레드 노벨의 사망일인 12월 10일에 스톡홀름에서 수여된다. 2007년의 노벨 물리학상은 프랑스의 알베르 페르와 독일의 페터 그륀베르크가 거대 자기저항의 발견에 대한 공로로 공동 수상하였고, 상금인 1천만 스웨덴 크로나를 나누어 가졌다. 노벨 물리학상은 사람들이 그 과학자의 업적의 중요성을 알기까지의 시간이 걸리기 때문에, 다른 한 편으로는 시간과의 싸움이라고 말할 수 있다. 예를 들어 1983년 노벨 물리학상 수상자인 수브라마니안 찬드라세카르의 경우 그 이론은 이미 1930년에 이미 발표하였지만 사람들에게 인정을 받지 못하여 50여년이 지나서야 상을 받을 수가 있었다. 또한 2013년 노벨 물리학상 수상자인 피터 힉스와 프랑수아 앙글레르의 경우 그의 이론을 검증할 수 있게 되는 과학기술이 발전하기 까지 오랜 시간이 걸려, 49년 뒤 그의 업적이 사실로 확인되어 노벨상을 받게 되었다. 그래서 많은 이론과 발견이 사람들에게 중요성을 인정받았지만, 그 이론이나 발견을 발표한 과학자가 이미 죽어버렸기에 노벨 물리학상을 받지 못하는 안타까운 경우도 있다."
conreference_content = "피시통신은 개인용 컴퓨터(PC)를 다른 컴퓨터와 통신 회선으로 연결하여 자료를 주고 받는 것을 말한다. 개인용 컴퓨터끼리 서로 연결한 통신 형태도 포함되지만, 보통은 정보 서비스 제공을 위한 호스트 컴퓨터와 통신 장비를 설치하고 여기에 가입한 사람들이 개인용 컴퓨터로 접속하여 이용하는 형태의 전화 회선을 통한 통신 네트워크 서비스를 가리킨다. 이때 통신 회선은 주로 전화 모뎀을 통한 전화 회선(PSTN)이 사용되지만 ISDN 등의 다른 회선이 사용되는 경우도 있다. 개인용 컴퓨터가 보편화되면서 1990년대에 게시판과 대화방, 그리고 자료실을 제공하는 PC통신 서비스 회사가 설립되었다."


# 언어 분석
@pytest.mark.asyncio
async def test_analysis(analysis: AnalysisClient):
    r = await analysis.analysis(text=analysis_text, analysis_code=AnalysisCode.morp)
    assert r.data


# 문장 패러프레이즈 인식
@pytest.mark.asyncio
async def test_paraphrase(analysis: AnalysisClient):
    r = await analysis.paraphrase(sentences[0], sentences[1])
    assert r.data


# 어휘 정보
@pytest.mark.asyncio
async def test_wordinfo(analysis: AnalysisClient):
    r = await analysis.wordinfo(word=word_1)
    assert r.data


# 동음이의어 정보
@pytest.mark.asyncio
async def test_homonym(analysis: AnalysisClient):
    r = await analysis.homonym(word=word_1)
    assert r.data


# 다의어 정보
@pytest.mark.asyncio
async def test_polysemy(analysis: AnalysisClient):
    r = await analysis.polysemy(word=word_1)
    assert r.data


# 어휘 간 유사도 분석
@pytest.mark.asyncio
async def test_wordrel(analysis: AnalysisClient):
    r = await analysis.wordrel(first_word=word_1, second_word=word_2)
    assert r.data


# 개체 연결
@pytest.mark.asyncio
async def test_wordrel(analysis: AnalysisClient):
    r = await analysis.nelinking(contents=NE_text)
    assert r[0].data


# 상호참조 해결
@pytest.mark.asyncio
async def test_coreference(analysis: AnalysisClient):
    r = await analysis.coreference(text=conreference_content)
    assert r.data
