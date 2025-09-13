from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from .element import TextElement

@dataclass
class Paragraph(TextElement):
    """Paragraph element: stores inline text."""
    text: str

    def render(self) -> str:
        return self.text + "\n\n"

    def render_toc(self) -> str:
        # Paragraphs are not included in TOC
        return ""

@dataclass
class Heading(TextElement):
    """Heading element with a level (1..6)."""
    text: str
    level: int = 1

    def render(self) -> str:
        # Render as markdown-like heading for clarity
        prefix = '#' * max(1, min(6, self.level))
        return f"{prefix} {self.text}\n\n"

    def render_toc(self) -> str:
        indent = '  ' * (max(1, min(6, self.level)) - 1)
        return f"{indent}- {self.text}\n"

@dataclass
class Link(TextElement):
    """Hyperlink element."""
    text: str
    url: str
    title: Optional[str] = None

    def render(self) -> str:
        title_part = f" ({self.title})" if self.title else ""
        return f"[{self.text}]({self.url}){title_part}\n\n"

    def render_toc(self) -> str:
        return ""  # links not in TOC by default

@dataclass
class Image(TextElement):
    """Image element - stores alt text and source path/URL."""
    alt: str
    src: str
    caption: Optional[str] = None

    def render(self) -> str:
        caption_part = f"\n*{self.caption}*" if self.caption else ""
        return f"![{self.alt}]({self.src}){caption_part}\n\n"

    def render_toc(self) -> str:
        return ""  # images not in TOC by default
