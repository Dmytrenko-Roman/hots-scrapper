from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Optional


@dataclass
class HeroItem:
    id: Optional[int] = field(default=None)
    name: Optional[str] = field(default=None)
    title: Optional[str] = field(default=None)
    role: Optional[str] = field(default=None)
    type: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    difficulty: Optional[str] = field(default=None)
    card_portrait: Optional[str] = field(default=None)
    franchise: Optional[str] = field(default=None)
    href: Optional[str] = field(default=None)
    imported_at: Optional[datetime] = field(default=datetime.now())
