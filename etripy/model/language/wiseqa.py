from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from .analysis import AnalysisResult


@dataclass(frozen=True)
class BaseQAEtri:
    data: Dict[str, Any] = field(repr=False)
    """데이터 Dict"""


@dataclass(frozen=True)
class VQT:
    """의문사기반 질문유형"""

    qt: Optional[int] = field(repr=True, compare=True, default=None)
    """질문유형 코드(숫자)"""
    strQTClue: Optional[int] = field(repr=True, compare=True, default=None)
    """의문사 스트링"""


@dataclass(frozen=True)
class VQF:
    """질문초점 객체 배열"""

    strQF: Optional[int] = field(repr=True, compare=True, default=None)
    """질문초점 스트링"""
    dWeightQF: Optional[int] = field(repr=True, compare=True, default=None)
    """질문초점 신뢰도"""


@dataclass(frozen=True)
class VLAT:
    """어휘정답유형 객체 배열"""

    strLAT: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘정답유형"""
    vCompoundLATs: Optional[List[int]] = field(repr=True, compare=True, default=None)
    """어휘정답유형의 복합명사 형태 스트링 목록"""
    strID: Optional[str] = field(repr=True, compare=True, default=None)
    """어휘의 코드(의미 또는 개념망 ID)"""
    dConfidenceLAT: Optional[float] = field(repr=True, compare=True, default=None)
    """인식의 신뢰도"""


@dataclass(frozen=True)
class VSAT:
    """세분류 의미정답유형 객체 배열"""

    strSAT: Optional[str] = field(repr=True, compare=True, default=None)
    """의미정답유형 스트링"""
    expanse_SAT: Optional[List[int]] = field(repr=True, compare=True, default=None)
    """확장 의미정답유형 배열"""
    dConfidenceSAT: Optional[float] = field(repr=True, compare=True, default=None)
    """인식 신뢰도"""


@dataclass(frozen=True)
class VEntityInfo:
    """개체의 위키백과 정보"""

    strNormEntity: Optional[str] = field(repr=True, compare=True, default=None)
    """위키백과 타이틀로 정규화된 개체 스트링"""
    strExplain: Optional[str] = field(repr=True, compare=True, default=None)
    """타이틀의 정의문"""
    dWeightEn: Optional[float] = field(repr=True, compare=True, default=None)
    """모호성 해소 가중치"""


@dataclass(frozen=True)
class VSATRoot:
    """대분류 의미정답유형 객체 배열"""

    strSAT: Optional[str] = field(repr=True, compare=True, default=None)
    """의미정답유형 스트링"""
    expanse_SAT: Optional[List[int]] = field(repr=True, compare=True, default=None)
    """확장 의미정답유형 배열"""
    dConfidenceSAT: Optional[float] = field(repr=True, compare=True, default=None)
    """인식 신뢰도"""


@dataclass(frozen=True)
class VTitleTopic:
    """주요한 개체 정보 배열"""

    strEntity: Optional[str] = field(repr=True, compare=True, default=None)
    """개체 스트링"""
    strEntityType: Optional[str] = field(repr=True, compare=True, default=None)
    """개체의 NE 스트링"""
    dWeightTitle: Optional[float] = field(repr=True, compare=True, default=None)
    """개체 중요도"""
    vEntityInfo: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """개체의 위키백과 정보"""

    @property
    def VEntityInfo(self):
        """개체의 위키백과 정보"""
        return VEntityInfo(**self.vEntityInfo)


@dataclass(frozen=True)
class OrgQUnit:
    """질문분석 기본정보"""

    strQuestion: Optional[str] = field(repr=True, compare=True, default=None)
    """질문 스트링"""
    strTaggedQ: Optional[str] = field(repr=True, compare=True, default=None)
    """질문 태깅결과 스트링(lexico-semantic pattern 매칭을 위한 언어분석 결과 출력"""
    ndoc: Optional[Dict[str, Any]] = field(repr=True, compare=True, default=None)
    """질문의 언어분석 결과 객체"""
    vQTs: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """의문사기반 질문유형"""
    vQFs: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """질문초점 객체 배열"""
    vLATs: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """어휘정답유형 객체 배열"""
    vSATs: Optional[List[Dict[str, Any]]] = field(repr=True, compare=True, default=None)
    """세분류 의미정답유형 객체 배열"""
    vSATRoots: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """대분류 의미정답유형 객체 배열"""
    vTitles: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """주요한 개체 정보 배열"""
    vQTopic: Optional[List[Dict[str, Any]]] = field(
        repr=True, compare=True, default=None
    )
    """위키백과 타이틀 중 가장 중요한 타이틀"""
    answerConstraint: Optional[List[Any]] = field(repr=True, compare=True, default=None)
    dIntegrativeConf: Optional[float] = field(repr=True, compare=True, default=None)
    """LAT와 SAT의 통합 신뢰도 정보"""

    @property
    def Ndoc(self) -> AnalysisResult:
        """질문의 언어분석 결과 객체"""
        return AnalysisResult(data=self.ndoc, **self.ndoc)

    @property
    def VQTs(self) -> List[VQT]:
        """의문사기반 질문유형"""
        return [VQT(**vqt) for vqt in self.vQTs]

    @property
    def VQFs(self) -> List[VQF]:
        """질문초점 객체 배열"""
        return [VQF(**vqf) for vqf in self.vQFs]

    @property
    def VLATs(self) -> List[VLAT]:
        """어휘정답유형 객체 배열"""
        return [VLAT(**vlat) for vlat in self.vLATs]

    @property
    def VSATs(self) -> List[VSAT]:
        """어휘정답유형 객체 배열"""
        return [VSAT(**vsat) for vsat in self.vSATs]

    @property
    def VSATRoots(self) -> List[VSATRoot]:
        """대분류 의미정답유형 객체 배열"""
        return [VSATRoot(**vsatr) for vsatr in self.vSATRoots]

    @property
    def VTitles(self) -> List[VTitleTopic]:
        """주요한 개체 정보 배열"""
        return [VTitleTopic(**vtitle) for vtitle in self.vTitles]

    @property
    def VQTopic(self) -> List[VTitleTopic]:
        """위키백과 타이틀 중 가장 중요한 타이틀"""
        return [VTitleTopic(**vqtopic) for vqtopic in self.vQTopic]


@dataclass(frozen=True)
class OrgQInfo:
    """질문분석 기본정보"""

    orgQUnit: Dict[str, Any] = field(repr=True, compare=True, default=None)
    """원질문 정보 객체"""

    @property
    def OrgQUnit(self) -> OrgQUnit:
        """원질문 정보 객체"""
        return OrgQUnit(**self.orgQUnit)


@dataclass(frozen=True)
class AnsQType:
    """정답형태에 따른 질문유형 객체"""

    strQType4Chg: Optional[str] = field(repr=True, compare=True, default=None)
    """질문유형 스트링"""
    dWeightCQT: Optional[str] = field(repr=True, compare=True, default=None)
    """인식 신뢰도"""


@dataclass(frozen=True)
class VSemQType:
    """의미적 질문유형 객체"""

    strQType4Chg: Optional[str] = field(repr=True, compare=True, default=None)
    """질문유형 스트링"""
    dWeightCQT: Optional[str] = field(repr=True, compare=True, default=None)
    """인식 신뢰도"""


@dataclass(frozen=True)
class QClassification:
    """질문분류 정보 객체"""

    ansQType: Optional[Dict[str, Any]] = field(repr=True, compare=True, default=None)
    """정답형태에 따른 질문유형 객체"""
    vSemQType: Optional[Dict[str, Any]] = field(repr=True, compare=True, default=None)
    """의미적 질문유형 객체"""

    @property
    def AnsQType(self) -> AnsQType:
        """정답형태에 따른 질문유형 객체"""
        return AnsQType(**self.ansQType)

    @property
    def VSemQType(self) -> VSemQType:
        """의미적 질문유형 객체"""
        return VSemQType(**self.vSemQType)


@dataclass(frozen=True)
class WiseQAnalResult(BaseQAEtri):
    """질의응답 결과 객체"""

    @property
    def OrgQInfo(self) -> OrgQInfo:
        """질문분석 기본정보"""
        return OrgQInfo(**self.data["return_object"]["orgQInfo"])

    @property
    def QClassification(self) -> QClassification:
        return QClassification(**self.data["return_object"]["QClassification"])
