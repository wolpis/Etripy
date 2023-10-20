from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class BaseLanguageEtri:
    data: Dict[str, Any] = field(repr=False)
    """데이터 Dict"""


@dataclass(frozen=True)
class Morp:
    """형태소 분석 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    """형태소 ID (출현 순서)"""
    lemma: Optional[str] = field(repr=True, compare=True, default=None)
    """형태소"""
    type: Optional[str] = field(repr=True, compare=True, default=None)
    """형태소 태그"""
    position: Optional[int] = field(repr=True, compare=True, default=None)
    """문장에서의 byte position"""
    weight: Optional[float] = field(repr=True, compare=True, default=None)
    """형태소 분석 결과 신뢰도"""


@dataclass(frozen=True)
class MorpEval:
    id: Optional[int] = field(repr=True, compare=True, default=None)
    result: Optional[str] = field(repr=True, compare=True, default=None)
    target: Optional[str] = field(repr=True, compare=True, default=None)
    word_id: Optional[int] = field(repr=True, compare=True, default=None)
    m_begin: Optional[int] = field(repr=True, compare=True, default=None)
    m_end: Optional[int] = field(repr=True, compare=True, default=None)


@dataclass(frozen=True)
class Wsd:
    """어휘의미 분석 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    """WSD 대상 ID (출현 순서)"""
    text: Optional[str] = field(repr=True, compare=True, default=None)
    """WSD 대상 어휘 텍스트"""
    type: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘 형태소 태그"""
    scode: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 표준국어대사전 어깨번호 (동형이의어 분석 시 2자리, 다의어 분석 시 6자리)"""
    weight: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘의 어휘의미 분석 결과 신뢰도"""
    position: Optional[int] = field(repr=True, compare=True, default=None)
    """문장에서의 byte position"""
    begin: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘의 첫 형태소의 ID"""
    end: Optional[int] = field(repr=True, compare=True, default=None)
    """어휘의 끝 형태소의 ID"""


@dataclass(frozen=True)
class Word:
    """어절 정보 분석 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    """어절의 ID (출현 순서)"""
    text: Optional[str] = field(repr=True, compare=True, default=None)
    """어절의 대상 텍스트"""
    type: Optional[str] = field(repr=True, compare=True, default=None)
    """어절 타입"""
    begin: Optional[int] = field(repr=True, compare=True, default=None)
    """어절을 구형하는 첫 형태소 ID"""
    end: Optional[int] = field(repr=True, compare=True, default=None)
    """어절을 구형하는 끝 형태소 ID"""


@dataclass(frozen=True)
class Ne:
    """개체명 정보 인식 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    """개체명 ID (출현 순서)"""
    text: Optional[str] = field(repr=True, compare=True, default=None)
    """개체명 어휘"""
    type: Optional[str] = field(repr=True, compare=True, default=None)
    """개체명 타입"""
    begin: Optional[int] = field(repr=True, compare=True, default=None)
    """개체명을 구성하는 첫 형태소의 ID"""
    end: Optional[int] = field(repr=True, compare=True, default=None)
    """개체명을 구성하는 끝 형태소의 ID"""
    weight: Optional[float] = field(repr=True, compare=True, default=None)
    """개체명 인식 결과 신뢰도"""
    common_noun: Optional[int] = field(repr=True, compare=True, default=None)
    """고유명사인 경우 0 일반명사인 경우 1"""


@dataclass(frozen=True)
class Dependency:
    """의존구문 분석 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    """어절의 ID (출현 순서)"""
    text: Optional[str] = field(repr=True, compare=True, default=None)
    """의존구문 텍스트"""
    head: Optional[int] = field(repr=True, compare=True, default=None)
    """부모 어절의 ID"""
    label: Optional[str] = field(repr=True, compare=True, default=None)
    """의존관계"""
    mod: Optional[List[int]] = field(repr=True, compare=True, default=None)
    """자식 어절들의 ID"""
    weight: Optional[float] = field(repr=True, compare=True, default=None)
    """의존구문 분석 결과 신뢰도"""


@dataclass(frozen=True)
class PhraseDependency:
    id: Optional[int] = field(repr=True, compare=True, default=None)
    label: Optional[str] = field(repr=True, compare=True, default=None)
    text: Optional[str] = field(repr=True, compare=True, default=None)
    begin: Optional[int] = field(repr=True, compare=True, default=None)
    end: Optional[int] = field(repr=True, compare=True, default=None)
    key_begin: Optional[int] = field(repr=True, compare=True, default=None)
    head_phrase: Optional[int] = field(repr=True, compare=True, default=None)
    sub_phrase: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    weight: Optional[float] = field(repr=True, compare=True, default=None)
    element: Optional[List[Any]] = field(repr=True, compare=True, default=None)


@dataclass(frozen=True)
class SrlArgument:
    """논항 정보"""

    type: Optional[str] = field(repr=True, compare=True, default=None)
    """논항 타입 정보"""
    word_id: Optional[int] = field(repr=True, compare=True, default=None)
    """논항 어절 ID"""
    text: Optional[str] = field(repr=True, compare=True, default=None)
    """논항 대상 어절의 텍스트"""
    weight: Optional[float] = field(repr=True, compare=True, default=None)
    """논항 분석에 대한 신뢰도"""


@dataclass(frozen=True)
class Srl:
    """의미역 분석 결과"""

    verb: Optional[str] = field(repr=True, compare=True, default=None)
    """대상 용언(predicate)"""
    sense: Optional[int] = field(repr=True, compare=True, default=None)
    """용언에 대한 의미 번호"""
    word_id: Optional[int] = field(repr=True, compare=True, default=None)
    """용언 어절 ID"""
    weight: Optional[float] = field(repr=True, compare=True, default=None)
    """결과에 대한 신뢰도"""
    argument: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """논항 정보"""

    @property
    def Argument(self) -> List[SrlArgument]:
        """논항 정보"""
        return [SrlArgument(**argument) for argument in self.argument]


@dataclass(frozen=True)
class Title:
    text: Optional[str] = field(repr=True, compare=True, default=None)
    NE: Optional[str] = field(repr=True, compare=True, default=None)


@dataclass(frozen=True)
class Sentence:
    id: Optional[int] = field(repr=True, compare=True, default=None)
    reserve_str: Optional[str] = field(repr=True, compare=True, default=None)
    """예비 공간으로 현재는 사용 안함."""
    text: Optional[str] = field(repr=True, compare=True, default=None)
    """분석한 원 문장"""
    morp: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """형태소 분석 결과"""
    morp_eval: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    WSD: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """어휘의미 분석 결과"""
    word: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """어절 정보 분석 결과"""
    NE: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """개체명 정보 인식 결과"""
    NE_Link: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    chunk: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    dependency: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """의존구문 분석 결과"""
    phrase_dependency: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    SRL: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """의미역 분석 결과"""
    relation: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    SA: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    ZA: Optional[List[Any]] = field(repr=True, compare=True, default=None)

    @property
    def Morp(self) -> List[Morp]:
        """형태소 분석 결과"""
        return [Morp(**morp) for morp in self.morp]

    @property
    def MorpEval(self) -> List[MorpEval]:
        return [MorpEval(**morp_eval) for morp_eval in self.morp_eval]

    @property
    def Wsd(self) -> List[Wsd]:
        """어휘의미 분석 결과"""
        return [Wsd(**wsd) for wsd in self.WSD]

    @property
    def Word(self) -> List[Word]:
        """어절 정보 분석 결과"""
        return [Word(**word) for word in self.word]

    @property
    def Ne(self) -> List[Ne]:
        """개체명 정보 인식 결과"""
        return [Ne(**ne) for ne in self.NE]

    @property
    def Dependency(self) -> List[Dependency]:
        """의존구문 분석 결과"""
        return [Dependency(**dependency) for dependency in self.dependency]

    @property
    def PhraseDependency(self) -> List[PhraseDependency]:
        return [PhraseDependency(**pb) for pb in self.phrase_dependency]

    @property
    def Srl(self) -> List[Srl]:
        """의미역 분석 결과"""
        return [Srl(**srl) for srl in self.SRL]


@dataclass(frozen=True)
class Analysis(BaseLanguageEtri):
    doc_id: Optional[str] = field(repr=True, compare=True, default=None)
    DCT: Optional[str] = field(repr=True, compare=True, default=None)
    category: Optional[str] = field(repr=True, compare=True, default=None)
    category_weight: Optional[int] = field(repr=True, compare=True, default=None)
    title: Optional[Dict[str, str]] = field(repr=True, compare=True, default=None)
    metaInfo: Optional[Dict[Any, Any]] = field(repr=True, compare=True, default=None)
    paragraphInfo: Optional[List[str]] = field(repr=True, compare=True, default=None)
    sentence: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    entity: Optional[List[Any]] = field(repr=True, compare=True, default=None)

    @property
    def Sentence(self) -> List[Sentence]:
        return [Sentence(**sentence) for sentence in self.sentence]

    @property
    def Title(self) -> Title:
        return Title(**self.title)
