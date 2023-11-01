from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class BaseLanguageEtri:
    data: Dict[str, Any] = field(repr=False)
    """데이터 Dict"""


@dataclass(frozen=True)
class BaseQAEtri:
    data: Dict[str, Any] = field(repr=False)
    """데이터 Dict"""
