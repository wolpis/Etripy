from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .base import BaseLanguageEtri


@dataclass(frozen=True)
class Morp:
    """형태소 분석 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    lemma: Optional[str] = field(repr=True, compare=True, default=None)
    type: Optional[str] = field(repr=True, compare=True, default=None)
    position: Optional[int] = field(repr=True, compare=True, default=None)
    weight: Optional[float] = field(repr=True, compare=True, default=None)


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
    text: Optional[str] = field(repr=True, compare=True, default=None)
    type: Optional[str] = field(repr=True, compare=True, default=None)
    scode: Optional[str] = field(repr=True, compare=True, default=None)
    weight: Optional[int] = field(repr=True, compare=True, default=None)
    position: Optional[int] = field(repr=True, compare=True, default=None)
    begin: Optional[int] = field(repr=True, compare=True, default=None)
    end: Optional[int] = field(repr=True, compare=True, default=None)


@dataclass(frozen=True)
class Word:
    """어절 정보 분석 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    text: Optional[str] = field(repr=True, compare=True, default=None)
    type: Optional[str] = field(repr=True, compare=True, default=None)
    begin: Optional[int] = field(repr=True, compare=True, default=None)
    end: Optional[int] = field(repr=True, compare=True, default=None)


@dataclass(frozen=True)
class Ne:
    """개체명 정보 인식 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    text: Optional[str] = field(repr=True, compare=True, default=None)
    type: Optional[str] = field(repr=True, compare=True, default=None)
    begin: Optional[int] = field(repr=True, compare=True, default=None)
    end: Optional[int] = field(repr=True, compare=True, default=None)
    weight: Optional[float] = field(repr=True, compare=True, default=None)
    common_noun: Optional[int] = field(repr=True, compare=True, default=None)


@dataclass(frozen=True)
class Dependency:
    """의존구문 분석 결과"""

    id: Optional[int] = field(repr=True, compare=True, default=None)
    text: Optional[str] = field(repr=True, compare=True, default=None)
    head: Optional[int] = field(repr=True, compare=True, default=None)
    label: Optional[str] = field(repr=True, compare=True, default=None)
    mod: Optional[List[int]] = field(repr=True, compare=True, default=None)
    weight: Optional[float] = field(repr=True, compare=True, default=None)


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
    word_id: Optional[int] = field(repr=True, compare=True, default=None)
    text: Optional[str] = field(repr=True, compare=True, default=None)
    weight: Optional[float] = field(repr=True, compare=True, default=None)


@dataclass(frozen=True)
class Srl:
    """의미역 분석 결과"""

    verb: Optional[str] = field(repr=True, compare=True, default=None)
    sense: Optional[int] = field(repr=True, compare=True, default=None)
    word_id: Optional[int] = field(repr=True, compare=True, default=None)
    weight: Optional[float] = field(repr=True, compare=True, default=None)
    argument: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )

    @property
    def Argument(self) -> List[SrlArgument]:
        """논항 정보"""
        if self.argument is None:
            return []
        return [SrlArgument(**argument) for argument in self.argument]


@dataclass(frozen=True)
class Title:
    text: Optional[str] = field(repr=True, compare=True, default=None)
    NE: Optional[str] = field(repr=True, compare=True, default=None)


@dataclass(frozen=True)
class Sentence:
    id: Optional[int] = field(repr=True, compare=True, default=None)
    reserve_str: Optional[str] = field(repr=True, compare=True, default=None)
    text: Optional[str] = field(repr=True, compare=True, default=None)
    morp: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    morp_eval: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    WSD: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    word: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    NE: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    NE_Link: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    chunk: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    dependency: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    phrase_dependency: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    SRL: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    relation: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    SA: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    ZA: Optional[List[Any]] = field(repr=True, compare=True, default=None)

    @property
    def Morp(self) -> List[Morp]:
        """형태소 분석 결과"""
        if self.morp is None:
            return []
        return [Morp(**morp) for morp in self.morp]

    @property
    def MorpEval(self) -> List[MorpEval]:
        if self.morp_eval is None:
            return []
        return [MorpEval(**morp_eval) for morp_eval in self.morp_eval]

    @property
    def Wsd(self) -> List[Wsd]:
        """어휘의미 분석 결과"""
        if self.WSD is None:
            return []
        return [Wsd(**wsd) for wsd in self.WSD]

    @property
    def Word(self) -> List[Word]:
        """어절 정보 분석 결과"""
        if self.word is None:
            return []
        return [Word(**word) for word in self.word]

    @property
    def Ne(self) -> List[Ne]:
        """개체명 정보 인식 결과"""
        if self.NE is None:
            return []
        return [Ne(**ne) for ne in self.NE]

    @property
    def Dependency(self) -> List[Dependency]:
        """의존구문 분석 결과"""
        if self.dependency is None:
            return []
        return [Dependency(**dependency) for dependency in self.dependency]

    @property
    def PhraseDependency(self) -> List[PhraseDependency]:
        if self.phrase_dependency is None:
            return []
        return [PhraseDependency(**pb) for pb in self.phrase_dependency]

    @property
    def Srl(self) -> List[Srl]:
        """의미역 분석 결과"""
        if self.SRL is None:
            return []
        return [Srl(**srl) for srl in self.SRL]


@dataclass(frozen=True)
class AnalysisResult(BaseLanguageEtri):
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
        if self.sentence is None:
            return []
        return [Sentence(**sentence) for sentence in self.sentence]

    @property
    def Title(self) -> Title:
        if self.title is None:
            return Title()
        return Title(**self.title)
