from typing import List
from .base import TextElement


class Text:
    """
    Root class representing a structured text container.
    Can hold paragraphs, headings, links, and images.
    """

    def __init__(self):
        self.elements: List[TextElement] = []

    def add(self, element: TextElement):
        """Add a new element to the text."""
        self.elements.append(element)

    def remove(self, index: int):
        """Remove element by index."""
        if 0 <= index < len(self.elements):
            del self.elements[index]

    def move(self, old_index: int, new_index: int):
        """Reorder an element from old_index to new_index."""
        if 0 <= old_index < len(self.elements):
            element = self.elements.pop(old_index)
            self.elements.insert(new_index, element)

    def __str__(self) -> str:
        """Render the entire text document."""
        return "".join(el.render() for el in self.elements)

    def generate_toc(self) -> str:
        """
        Generate a table of contents (TOC) based on headings.
        Indentation depends on heading level.
        """
        toc_lines = []
        for el in self.elements:
            if el.is_heading():
                indent = "  " * (el.level - 1)
                toc_lines.append(f"{indent}- {el.content}")
        return "\n".join(toc_lines)
