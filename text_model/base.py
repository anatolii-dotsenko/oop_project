from abc import ABC, abstractmethod


class TextElement(ABC):
    """
    Abstract base class for all text elements.
    Defines the interface for rendering and identifying elements.
    """

    @abstractmethod
    def render(self) -> str:
        """Return the string representation of the element."""
        pass

    @abstractmethod
    def is_heading(self) -> bool:
        """Return True if this element is a heading."""
        pass
