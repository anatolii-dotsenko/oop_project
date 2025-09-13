from __future__ import annotations
from typing import Protocol, runtime_checkable

@runtime_checkable
class Ability(Protocol):
    """Protocol for abilities that a character can use."""
    name: str
    def use(self, user, target): ...
