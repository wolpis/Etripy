from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class VideoParseResult:
    num: Optional[int] = field(repr=True, compare=True, default=None)
    code: Optional[int] = field(repr=True, compare=True, default=None)
    msg: Optional[str] = field(repr=True, compare=True, default=None)
    frame: Optional[list[int]] = field(repr=True, compare=True, default=None)
    time: Optional[list[int]] = field(repr=True, compare=True, default=None)
