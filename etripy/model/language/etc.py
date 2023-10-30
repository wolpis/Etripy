from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class BaseLanguageEtri:
    data: Dict[str, Any] = field(repr=False)
    """데이터 Dict"""


####################### 패러플라이즈 #######################
@dataclass(frozen=True)
class ParaphraseResult(BaseLanguageEtri):
    result: Optional[str] = field(repr=True, compare=True, default=None)
    """패러프레이즈 분석 결과"""

    @property
    def is_paraphrase(self) -> bool:
        """패러프레이즈 분석 결과"""
        if self.result == "paraphrase":
            return True
        else:
            return False


####################### 어휘 정보 #######################
@dataclass(frozen=True)
class MetaInfo:
    Title: Optional[str] = field(repr=True, compare=True, default=None)
    """Open APIs의 타이틀 명"""
    Link: Optional[str] = field(repr=True, compare=True, default=None)
    """해당 Open APIs를 사용하기 위한 URL 정보"""


@dataclass(frozen=True)
class WordInfoList:
    """어휘의 상세 정보"""

    PolysemyCode: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘의 다의어 코드 (2자리 숫자)"""
    Definition: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 의미 정보"""
    POS: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 품사"""
    Hypernym: Optional[List[str]] = field(repr=True, compare=True, default=None)
    """어휘의 상위 어휘 정보"""
    Hypornym: Optional[List[str]] = field(repr=True, compare=True, default=None)
    """어휘의 하위 어휘 정보"""


@dataclass(frozen=True)
class WordInfo:
    """어휘의 상세 정보"""

    Word: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 원문자열"""
    HomonymCode: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 동음이의어 코드 (2자리 숫자)"""
    WordInfo: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """어휘의 상세 정보"""
    Synonym: Optional[List[str]] = field(repr=True, compare=True, default=None)
    """어휘의 유의어 어휘 정보"""
    Antonym: Optional[List[str]] = field(repr=True, compare=True, default=None)
    """어휘의 반의어 어휘 정보"""

    @property
    def WordInfoList(self) -> List[WordInfoList]:
        """어휘의 상세 정보"""
        return [WordInfoList(**wi) for wi in self.WordInfo]


@dataclass(frozen=True)
class WordResult(BaseLanguageEtri):
    """어휘 정보 결과"""

    @property
    def MetaInfo(self) -> MetaInfo:
        """Open APIs의 정보"""
        return MetaInfo(**self.data["return_object"]["MetaInfo"])

    @property
    def WordInfo(self) -> List[WordInfo]:
        """어휘의 상세 정보"""
        return [
            WordInfo(**wordinfo)
            for wordinfo in self.data["return_object"]["WWN WordInfo"]
        ]


####################### 동음이의어 #######################
@dataclass(frozen=True)
class Homonym:
    word: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 원문자열"""
    homonym_code: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 동음이의어 코드 (표준국어대사전 어깨번호)"""
    polysemy_code: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 다의어 코드 (표준국어대사전 어깨번호)"""
    word_class: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 품사"""
    description: Optional[str] = field(repr=True, compare=True, default=None)
    """의미 정보"""


@dataclass(frozen=True)
class HomonymResult(BaseLanguageEtri):
    """동음이의어 정보 결과"""

    homonym: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """동음이의어 정보"""

    @property
    def Homonym(self) -> List[Homonym]:
        """동음이의어 정보"""
        return [Homonym(**homonym) for homonym in self.homonym]


####################### 다의어 #######################
@dataclass(frozen=True)
class Polysemy:
    word: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 원문자열"""
    homonym_code: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 동음이의어 코드 (표준국어대사전 어깨번호)"""
    polysemy_code: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 다의어 코드 (표준국어대사전 어깨번호)"""
    word_class: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 품사"""
    description: Optional[str] = field(repr=True, compare=True, default=None)
    """의미 정보"""


@dataclass(frozen=True)
class PolysemyResult(BaseLanguageEtri):
    """다의어 정보 결과"""

    polysemy: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """다의어 정보"""

    @property
    def Polysemy(self) -> List[Polysemy]:
        """다의어 정보"""
        return [Polysemy(**polysemy) for polysemy in self.polysemy]


####################### 어휘 간 유사도 분석 #######################
@dataclass(frozen=True)
class SimilarityList:
    Algorithm: Optional[str] = field(repr=True, compare=True, default=None)
    """거리 유사도 알고리즘"""
    SimScore: Optional[float] = field(repr=True, compare=True, default=None)
    """거리 유사도 신뢰도"""


@dataclass(frozen=True)
class WordRelInfo_:
    ShortedPath: Optional[List[str]] = field(repr=True, compare=True, default=None)
    """가장 가까운 연결 어휘 경로 정보"""
    Distance: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘 경로 거리 정보 (숫자)"""
    Similarity: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """어휘 간 거리 유사도"""

    @property
    def SimilarityList(self) -> List[SimilarityList]:
        """어휘 간 거리 유사도"""
        return [SimilarityList(**sim) for sim in self.Similarity]


@dataclass(frozen=True)
class FirstWordInfo_:
    """첫 번째 어휘 정보"""

    Word: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 원문자열"""
    HomonymCode: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘의 동음이의어 코드 (2자리 숫자)"""
    PolysemyCode: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘의 다의어 코드 (2자리 숫자)"""
    Definition: Optional[str] = field(repr=True, compare=True, default=None)
    """의미 정보"""
    POS: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 품사"""


@dataclass(frozen=True)
class SecondWordInfo_:
    """두 번째 어휘 정보"""

    Word: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 원문자열"""
    HomonymCode: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘의 동음이의어 코드 (2자리 숫자)"""
    PolysemyCode: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘의 다의어 코드 (2자리 숫자)"""
    Definition: Optional[str] = field(repr=True, compare=True, default=None)
    """의미 정보"""
    POS: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 품사"""


@dataclass(frozen=True)
class WordRelInfo:
    """어휘 간 유사도 분석 정보"""

    FirstWordInfo: Optional[Dict[str, Any]] = field(
        repr=True, compare=True, default=None
    )
    """첫 번째 어휘 정보"""
    SecondWordInfo: Optional[Dict[str, Any]] = field(
        repr=True, compare=True, default=None
    )
    """두 번째 어휘 정보"""
    WordRelInfo: Optional[Dict[str, Any]] = field(repr=True, compare=True, default=None)

    @property
    def FirstWordInfo_(self) -> FirstWordInfo_:
        return FirstWordInfo_(**self.FirstWordInfo)

    @property
    def SecondWordInfo_(self) -> SecondWordInfo_:
        return SecondWordInfo_(**self.SecondWordInfo)

    @property
    def WordRelInfo_(self) -> WordRelInfo_:
        return WordRelInfo_(**self.WordRelInfo)


@dataclass(frozen=True)
class WordRelResult(BaseLanguageEtri):
    @property
    def MetaInfo(self) -> MetaInfo:
        """Open APIs의 정보"""
        return MetaInfo(**self.data["return_object"]["MetaInfo"])

    @property
    def WordRelInfo(self) -> WordRelInfo:
        """어휘 간 유사도 분석 정보"""
        return WordRelInfo(**self.data["return_object"]["WWN WordRelInfo"])


####################### 어휘관계 분석 #######################
@dataclass(frozen=True)
class NELinkingMention:
    """개체 연결 정보 배열"""

    article_id: Optional[int] = field(repr=True, compare=True, default=None)
    """연결된 위키피디아 타이틀 ID"""
    definition: Optional[str] = field(repr=True, compare=True, default=None)
    """연결 개체의 정의문(위키피디아 첫 문장(단락))"""
    mention: Optional[str] = field(repr=True, compare=True, default=None)
    """인식된 멘션"""
    prediction: Optional[bool] = field(repr=True, compare=True, default=None)
    """이진분류에서의 예측결과(true이면, 개체연결이 올바른 분류라는 의미)"""
    s_pos: Optional[int] = field(repr=True, compare=True, default=None)
    """전체 입력에서 인식된 멘션의 시작 위치"""
    score: Optional[float] = field(repr=True, compare=True, default=None)
    """개체연결에 대한 점수"""
    title: Optional[str] = field(repr=True, compare=True, default=None)
    """인식된 개체의 제목"""
    type: Optional[str] = field(repr=True, compare=True, default=None)
    """인식된 개체 태그"""
    url: Optional[str] = field(repr=True, compare=True, default=None)
    """위키피디아 연결 URL"""


@dataclass(frozen=True)
class NELinkingResult(BaseLanguageEtri):
    """개체 연결 분석 결과"""

    mentions: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """개체 연결 정보 배열"""
    sent_id: Optional[int] = field(repr=True, compare=True, default=None)
    """문장 번호"""
    sentence: Optional[str] = field(repr=True, compare=True, default=None)
    """문장 원문"""
    t_sentence: Optional[str] = field(repr=True, compare=True, default=None)
    """개체연결 ID가 부착된 문장"""

    @property
    def Mentions(self) -> List[NELinkingMention]:
        """개체 연결 정보 배열"""
        return [NELinkingMention(**mention) for mention in self.mentions]


####################### 상호참조 해결 #######################
@dataclass(frozen=True)
class CoreferenceMention:
    id: Optional[int] = field(repr=True, compare=True, default=None)
    text: Optional[str] = field(repr=True, compare=True, default=None)
    sent_id: Optional[int] = field(repr=True, compare=True, default=None)
    """문장 ID"""
    start_eid: Optional[int] = field(repr=True, compare=True, default=None)
    """문장 내 text의 시작 어절 ID"""
    end_eid: Optional[int] = field(repr=True, compare=True, default=None)
    """문장 내 text의 종료 어절 ID"""
    start_eid_short: Optional[int] = field(repr=True, compare=True, default=None)
    """문장 내 text_short의 시작 어절 ID"""
    end_eid_short: Optional[int] = field(repr=True, compare=True, default=None)
    """문장 내 text_short의 종료 어절 ID"""
    text_short: Optional[str] = field(repr=True, compare=True, default=None)
    """짧게 표현된 멘션 텍스트"""


@dataclass(frozen=True)
class CoreferenceEntity:
    """어휘관계 분석 결과"""

    animacy: Optional[str] = field(repr=True, compare=True, default=None)
    mention: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """인식된 멘션 목록"""
    gender: Optional[str] = field(repr=True, compare=True, default=None)
    number: Optional[str] = field(repr=True, compare=True, default=None)
    person: Optional[str] = field(repr=True, compare=True, default=None)
    type: Optional[str] = field(repr=True, compare=True, default=None)
    id: Optional[int] = field(repr=True, compare=True, default=None)

    @property
    def Mention(self) -> List[CoreferenceMention]:
        """인식된 멘션 목록"""
        return [CoreferenceMention(**mention) for mention in self.mention]


@dataclass(frozen=True)
class CoreferenceResult(BaseLanguageEtri):
    entity: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """어휘관계 분석 결과"""

    @property
    def Entity(self) -> List[CoreferenceEntity]:
        """어휘관계 분석 결과"""
        entity_ = []
        for entity in self.entity:
            entity["animacy"] = entity["animacy "]
            del entity["animacy "]
            entity_.append(entity)
        return [CoreferenceEntity(**entity) for entity in entity_]
