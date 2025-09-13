from __future__ import annotations
from typing import List, Iterable
from .element import TextElement

class Text:
    """Container for TextElements (paragraphs, headings, links, images).
    
    Responsibilities:
    - hold ordered elements
    - provide add/remove/reorder operations
    - render full article to string
    - render table of contents (only headings) with indentation
    """
    def __init__(self, title: str = "") -> None:
        self.title = title
        self._elements: List[TextElement] = []

    def add(self, element: TextElement, position: int | None = None) -> None:
        """Add an element at the end or at given position."""
        if position is None:
            self._elements.append(element)
        else:
            self._elements.insert(position, element)

    def remove(self, element: TextElement) -> None:
        """Remove first matching element."""
        self._elements.remove(element)

    def move(self, from_index: int, to_index: int) -> None:
        """Move element within container (preserves element identity)."""
        elem = self._elements.pop(from_index)
        self._elements.insert(to_index, elem)

    def extend(self, elements: Iterable[TextElement]) -> None:
        """Add multiple elements preserving order."""
        self._elements.extend(elements)

    def render(self) -> str:
        """Render full article as a single string (title + elements)."""
        parts = []
        if self.title:
            parts.append(f"# {self.title}\n\n")
        for el in self._elements:
            parts.append(el.render())
        return ''.join(parts)

    def render_toc(self) -> str:
        """Render a simple table of contents based on headings only."""
        lines = []
        if self.title:
            lines.append(f"Contents for: {self.title}\n\n")
        for el in self._elements:
            toc = el.render_toc()
            if toc:
                lines.append(toc)
        return ''.join(lines)
