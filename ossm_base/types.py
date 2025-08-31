from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import Optional


@dataclass
class Stimulus:
    data: Dict[str, Any]
    timestamp: Optional[float] = None

@dataclass
class Observable:
    data: Optional[Dict[str, Any]] = None
    source: str = None
    timestamp: Optional[float] = None