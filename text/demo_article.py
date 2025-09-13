from .elements_impl import Paragraph, Heading, Link, Image
from .container import Text

def build_sample_article() -> Text:
    article = Text(title="Designing with Classes: short guide")
    article.add(Heading("Introduction", level=1))
    article.add(Paragraph("This short article demonstrates a minimal text abstraction system."))
    article.add(Heading("Principles", level=2))
    article.add(Paragraph("Classes should be simple, focused, and named clearly."))
    article.add(Heading("Example: Product", level=2))
    article.add(Paragraph("Product has name, description and price. Use minimal modeling."))
    article.add(Link(text="Further reading", url="https://example.com", title="example"))
    article.add(Image(alt="diagram", src="/images/diagram.png", caption="Simple diagram"))
    article.add(Heading("Conclusion", level=1))
    article.add(Paragraph("Balance between simplicity and flexibility is key."))
    return article

if __name__ == '__main__':
    article = build_sample_article()
    print(article.render())
    print('\n--- TABLE OF CONTENTS ---\n')
    print(article.render_toc())
