from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class ObjectDetectResult:
    data: Optional[dict[str, str]] = field(repr=True, compare=True, default=None)
    """이미지 객체 분석 결과"""

    @property
    def class__(self) -> str:
        """인식 된 객체명"""
        return self.data["class"]

    @property
    def confidence(self) -> str:
        """신뢰도"""
        return self.data["confidence"]

    @property
    def x(self) -> str:
        """x 좌표"""
        return self.data["x"]

    @property
    def y(self) -> str:
        """y 좌표"""
        return self.data["y"]

    @property
    def width(self) -> str:
        """길이"""
        return self.data["width"]

    @property
    def height(self) -> str:
        """높이"""
        return self.data["height"]


@dataclass(frozen=True)
class HumanParsingResult:
    data: Optional[dict[str, str]] = field(repr=True, compare=True, default=None)
    """사람 속성 검출 분석 결과"""

    @property
    def num(self) -> str:
        """여러 사람일 경우의 사람 ID"""
        return self.data["num"]

    @property
    def position(self) -> str:
        """사람의 위치 정보 - 박스 좌표"""
        return self.data["position"]

    @property
    def hat_mask(self) -> Optional[str]:
        """모자 부분 영역의 Contour 좌표 정보"""
        return self.data["hat mask"]

    @property
    def hat_color(self) -> Optional[str]:
        """모자 부분 영역의 색상 정보(RGB)"""
        return self.data["hat color"]

    @property
    def hair_mask(self) -> Optional[str]:
        """머리 부분 영역의 Contour 좌표 정보"""
        return self.data["hair mask"]

    @property
    def hair_color(self) -> Optional[str]:
        """머리 부분 영역의 색상 정보(RGB)"""
        return self.data["hair color"]

    @property
    def upcloth_mask(self) -> Optional[str]:
        """상의 부분 영역의 Contour 좌표 정보"""
        return self.data["upcloth mask"]

    @property
    def upcloth_color(self) -> Optional[str]:
        """상의 부분 영역의 Contour 좌표 정보"""
        return self.data["upcloth color"]

    @property
    def dress_mask(self) -> Optional[str]:
        """드레스 부분 영역의 Contour 좌표 정보"""
        return self.data["dress mask"]

    @property
    def dress_color(self) -> Optional[str]:
        """드레스 부분 영역의 색상 정보(RGB)"""
        return self.data["dress color"]

    @property
    def coat_mask(self) -> Optional[str]:
        """코트 부분 영역의 Contour 좌표 정보"""
        return self.data["coat mask"]

    @property
    def coat_color(self) -> Optional[str]:
        """코트 부분 영역의 색상 정보(RGB)"""
        return self.data["coat color"]

    @property
    def pants_mask(self) -> Optional[str]:
        """바지 부분 영역의 Contour 좌표 정보"""
        return self.data["pants mask"]

    @property
    def pants_color(self) -> Optional[str]:
        """바지 부분 영역의 색상 정보(RGB)"""
        return self.data["pants color"]

    @property
    def skirt_mask(self) -> Optional[str]:
        """얼굴 영역 검출에 대한 신뢰도"""
        return self.data["skirt mask"]

    @property
    def skirt_color(self) -> Optional[str]:
        """스커트 부분 영역의 색상 정보(RGB)"""
        return self.data["skirt color"]


@dataclass(frozen=True)
class FaceDeIDResult:
    data: Optional[dict[str, str]] = field(repr=True, compare=True, default=None)
    """이미지 객체 분석 결과"""

    @property
    def conf(self) -> str:
        """얼굴 영역 검출에 대한 신뢰도"""
        return self.data["class"]

    @property
    def x(self) -> str:
        """x 좌표"""
        return self.data["x"]

    @property
    def y(self) -> str:
        """y 좌표"""
        return self.data["y"]

    @property
    def width(self) -> str:
        """길이"""
        return self.data["width"]

    @property
    def height(self) -> str:
        """높이"""
        return self.data["height"]


@dataclass(frozen=True)
class HumanStatusResult:
    data: Optional[dict[str, str]] = field(repr=True, compare=True, default=None)
    """이미지 객체 분석 결과"""
    img_url: Optional[str] = field(repr=True, compare=True, default=None)
    """분석된 이미지의 경로"""

    @property
    def class__(self) -> str:
        """검출된 사람의 상태"""
        return self.data["class"]

    @property
    def confidence(self) -> str:
        """사람 상태 인식에 대한 신뢰도"""
        return self.data["confidence"]

    @property
    def x(self) -> str:
        """x 좌표"""
        return self.data["x"]

    @property
    def y(self) -> str:
        """y 좌표"""
        return self.data["y"]

    @property
    def width(self) -> str:
        """길이"""
        return self.data["width"]

    @property
    def height(self) -> str:
        """높이"""
        return self.data["height"]

    @property
    def segm(self) -> list[int]:
        """다각형을 이용하여 사람의 영역을 표현하며 순서대로 다각형의 꼭짓점을 의미 [x1, y1, x2, y2, x3, y3, ....,xn, yn]"""
        return self.data["segm"]

    @property
    def key(self) -> list[float]:
        """검출된 사람의 자세 [x, y, c]*17. 총 17개의 점으로 사람의 자세를 표현하며 x,y,c는 각각 x 좌표, y 좌표, confidence 값이다."""
        return self.data["key"]
