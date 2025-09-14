from .base import TextElement


class Paragraph(TextElement):
    """Represents a paragraph of text."""

    def __init__(self, content: str):
        self.content = content

    def render(self) -> str:
        return self.content + "\n"

    def is_heading(self) -> bool:
        return False


class Heading(TextElement):
    """Represents a heading with a given level (1–6)."""

    def __init__(self, content: str, level: int = 1):
        if not (1 <= level <= 6):
            raise ValueError("Heading level must be between 1 and 6")
        self.content = content
        self.level = level

    def render(self) -> str:
        prefix = "#" * self.level
        return f"{prefix} {self.content}\n"

    def is_heading(self) -> bool:
        return True


class Link(TextElement):
    """Represents a hyperlink with label and target URL."""

    def __init__(self, label: str, url: str):
        self.label = label
        self.url = url

    def render(self) -> str:
        return f"[{self.label}]({self.url})\n"

    def is_heading(self) -> bool:
        return False


class Image(TextElement):
    """Represents an image with alt text and path/URL."""

    def __init__(self, alt_text: str, path: str):
        self.alt_text = alt_text
        self.path = path

    def render(self) -> str:
        return f"![{self.alt_text}]({self.path})\n"

    def is_heading(self) -> bool:
        return False
