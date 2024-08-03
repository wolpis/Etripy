from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class ObjectDetectResult:
    data: Optional[dict[str, str]] = field(repr=True, compare=True, default=None)
    """음성 언어 코드에 따른 음성인식 결과"""

    @property
    def class__(self):
        """인식 된 객체명"""
        return self.data["class"]

    @property
    def confidence(self):
        """신뢰도"""
        return self.data["confidence"]

    @property
    def x(self):
        """x 좌표"""
        return self.data["x"]

    @property
    def y(self):
        """y 좌표"""
        return self.data["y"]

    @property
    def width(self):
        """길이"""
        return self.data["width"]

    @property
    def height(self):
        """높이"""
        return self.data["height"]
