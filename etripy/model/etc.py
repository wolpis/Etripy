class AnalysisCode:
    """분석 타입을 반환하는 클래스입니다."""

    morp: str = "morp"
    """형태소 분석 (문어/구어)"""

    wsd: str = "wsd"
    """어휘의미 분석 (동음이의어 분석)(문어)"""

    wsd_poly: str = "wsd_poly"
    """어휘의미 분석 (다의어 분석)(문어)"""

    ner: str = "ner"
    """개체명 인식 (문어/구어)"""

    dparse: str = "dparse"
    """의존 구문 분석 (문어)"""

    srl: str = "srl"
    "의미역 인식 (문어)"


class WikiType:
    """질문 응답 엔진의 종류를 반환하는 클래스입니다."""

    irqa: str = "irqa"
    """언어분석 기반과 기계독해 기반의 질의응답을 통합한 질의응답 방식"""

    kbqa: str = "kbpa"
    """지식베이스 기반의 질의응답 방식"""

    hybridqa: str = "hybridqa"
    """"irqa와 kbqa를 통합한 질의응답 방식"""


class FileType:
    """행정문서 QA에서 한글 문서 확장자를 선언할때 사용하는 클래스입니다."""

    hwp: str = "hwp"
    """hwp 문서를 분석할 때 사용합니다."""

    hwpx: str = "hwpx"
    """hwpx 문서를 분석할 때 사용합니다."""


class LanguageCodeType:
    """음성인식의 입력 음성 언어 코드입니다."""

    korean: str = "korean"
    """한국어 음성인식 코드"""

    english: str = "english"
    """영어 음성인식 코드"""

    japanese: str = "japanese"
    """일본어 음성인식 코드"""

    chinese: str = "chinese"
    """중국어 음성인식 코드"""

    spanish: str = "spanish"
    """스페인어 음성인식 코드"""

    french: str = "french"
    """프랑스어 음성인식 코드"""

    german: str = "german"
    """독일어 음성인식 코드"""

    russian: str = "russian"
    """러시아어 음성인식 코드"""

    vietnam: str = "vietnam"
    """베트남어 음성인식 코드"""

    arabic: str = "arabic"
    """아랍어 음성인식 코드"""

    thailand: str = "thailand"
    """태국어 음성인식 코드"""

    portuguese: str = "portuguese"
    """포르투칼어 음성인식 코드"""

    malaysia: str = "malaysia"
    """말레이어 음성인식 코드"""

    indonesian: str = "indonesian"
    """인도네시아어 음성인식 코드"""

    cantonese: str = "cantonese"
    """광둥어 음성인식 코드"""
