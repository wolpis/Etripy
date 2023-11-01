from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .base import BaseQAEtri


####################### 기계 독해 #######################
@dataclass(frozen=True)
class MRCResult(BaseQAEtri):
    """기계독해 결과"""

    @property
    def answer(self) -> Optional[str]:
        """정답"""
        return self.data["answer"]

    @property
    def confidence(self) -> Optional[str]:
        """정답의 신뢰도"""
        return self.data["confidence"]

    @property
    def passage(self) -> Optional[str]:
        """요청한 단락"""
        return self.data["passage"]

    @property
    def question(self) -> Optional[str]:
        """요청한 질문"""
        return self.data["question"]

    @property
    def begin(self) -> Optional[int]:
        """단락 내에서 정답 시작 음절 인덱스"""
        return self.data["begin"]

    @property
    def end(self) -> Optional[int]:
        """단락 내에서 정답의 마지막 음절 인덱스"""
        return self.data["end"]


####################### 위키백과 #######################
@dataclass(frozen=True)
class IRInfo:
    """검색 정보"""

    wiki_title: Optional[str] = field(repr=True, compare=True, default=None)
    """검색 결과의 위키백과 타이틀"""
    sent: Optional[str] = field(repr=True, compare=True, default=None)
    """검색 단락"""
    url: Optional[str] = field(repr=True, compare=True, default=None)
    """위키 url"""


@dataclass(frozen=True)
class WikiAnswerInfo:
    """정답 정보"""

    rank: Optional[int] = field(repr=True, compare=True, default=None)
    """정답 순위"""
    answer: Optional[str] = field(repr=True, compare=True, default=None)
    """정답"""
    confidence: Optional[float] = field(repr=True, compare=True, default=None)
    """정답의 신뢰도"""
    url: Optional[List[str]] = field(repr=True, compare=True, default=None)
    """위키 url"""


@dataclass(frozen=True)
class WiKiResult(BaseQAEtri):
    """검색 정보 결과"""

    @property
    def IRInfo(self) -> Optional[List[IRInfo]]:
        """검색 정보"""
        return [
            IRInfo(**wiki) for wiki in self.data["return_object"]["WikiInfo"]["IRInfo"]
        ]

    @property
    def AnswerInfo(self) -> Optional[List[WikiAnswerInfo]]:
        """정답 정보"""
        return [
            WikiAnswerInfo(**wiki)
            for wiki in self.data["return_object"]["WiKiInfo"]["AnswerInfo"]
        ]


####################### 법률 QA #######################
@dataclass(frozen=True)
class LegalAnswerInfo:
    """응답결과 정보"""

    rank: Optional[int] = field(repr=True, compare=True, default=None)
    """정답/검색 순위"""
    answer: Optional[int] = field(repr=True, compare=True, default=None)
    """정답 (검색결과일 경우 빈 문자열)"""
    source: Optional[str] = field(repr=True, compare=True, default=None)
    """정답의 출처(법률명 및 조제목)"""
    clause: Optional[str] = field(repr=True, compare=True, default=None)
    """조 내용"""
    confidence: Optional[str] = field(repr=True, compare=True, default=None)
    """정답의 스코어"""


@dataclass(frozen=True)
class LegalResult(BaseQAEtri):
    """법률 QA 결과"""

    @property
    def AnswerInfo(self) -> List[LegalAnswerInfo]:
        """응답결과 정보"""
        return [
            LegalAnswerInfo(**answer)
            for answer in self.data["return_object"]["LegalInfo"]["AnswerInfo"]
        ]

    @property
    def RelatedQs(self) -> List[str]:
        """유사질문의 리스트 (비어있을 수 있음)"""
        return [self.data["return_object"]["LegalInfo"]["RelatedQs"]]


####################### 행정문서 QA #######################
@dataclass(frozen=True)
class DocUploadResult(BaseQAEtri):
    """등록된 파일 업로드 결과"""

    @property
    def doc_key(self) -> str:
        """등록된 파일에 대한 고유 document key"""
        return self.data["return_object"]["doc_key"]


@dataclass(frozen=True)
class DocInfo:
    """문서 분석 결과"""

    answer: Optional[str] = field(repr=True, compare=True, default=None)
    """정답"""
    passage: Optional[str] = field(repr=True, compare=True, default=None)
    """정답이 포함된 단락"""
    evidence: Optional[List[str]] = field(repr=True, compare=True, default=None)
    """정답의 근거 문장(리스트)"""
    confidence: Optional[float] = field(repr=True, compare=True, default=None)
    """신뢰도"""
    rank: Optional[int] = field(repr=True, compare=True, default=None)
    """순위"""


@dataclass(frozen=True)
class DocResult(BaseQAEtri):
    """등록된 파일의 분석 결과"""

    @property
    def DocInfo(self) -> List[DocInfo]:
        """문서 분석 결과"""
        return [DocInfo(**doc) for doc in self.data["return_object"]["DocInfo"]]

    @property
    def question(self) -> str:
        """질문"""
        return self.data["return_object"]["question"]
