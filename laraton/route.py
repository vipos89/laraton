from dataclasses import dataclass
from typing import Type


@dataclass
class Route:
    url: str
    controller: str
