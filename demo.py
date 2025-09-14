from text_model.text import Text
from text_model.elements import Paragraph, Heading, Link, Image


def main():
    article = Text()

    # Build an example article
    article.add(Heading("Python OOP Text Abstraction", level=1))
    article.add(Paragraph("This article demonstrates an object-oriented model "
                          "for representing text elements in Python."))

    article.add(Heading("Introduction", level=2))
    article.add(Paragraph("Object-oriented programming helps us build modular "
                          "and extensible systems."))
    article.add(Link("Learn more about OOP", "https://en.wikipedia.org/wiki/Object-oriented_programming"))

    article.add(Heading("Images in Text", level=2))
    article.add(Paragraph("We can also embed images as first-class elements."))
    article.add(Image("Example diagram", "diagram.png"))

    article.add(Heading("Conclusion", level=2))
    article.add(Paragraph("This design cleanly separates responsibilities and "
                          "keeps the system extensible."))

    # Render article
    print("=== ARTICLE ===")
    print(article)

    # Render table of contents
    print("=== TABLE OF CONTENTS ===")
    print(article.generate_toc())


if __name__ == "__main__":
    main()
