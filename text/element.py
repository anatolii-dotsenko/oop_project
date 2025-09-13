from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

@runtime_checkable
class TextElement(Protocol):
    """
    Protocol for elements that can be placed inside a Text container.
    Implementations must provide `render()` and `render_toc()`.
    """
    def render(self) -> str:...
    def render_toc(self) -> str:...
