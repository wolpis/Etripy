from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class VideoParseResult:
    num: Optional[int] = field(repr=True, compare=True, default=None)
    """장면분할의 처리 번호"""
    code: Optional[int] = field(repr=True, compare=True, default=None)
    """장면분할의 처리 결과 코드"""
    msg: Optional[str] = field(repr=True, compare=True, default=None)
    """장면분할의 처리 결과 메시지"""
    frame: Optional[list[int]] = field(repr=True, compare=True, default=None)
    """장면분할의 결과로 나온 총 분할시점의 숫자"""
    time: Optional[list[int]] = field(repr=True, compare=True, default=None)
    """분할된 구간의 시작 시점 (초)"""
