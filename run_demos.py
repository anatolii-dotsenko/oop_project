from text.demo_article import build_sample_article
from game.demo_battle import run_demo

def main():
    print('=== ARTICLE RENDER ===\n')
    article = build_sample_article()
    print(article.render())
    print('\n=== TABLE OF CONTENTS ===\n')
    print(article.render_toc())
    print('\n=== GAME SIMULATION ===\n')
    print(run_demo())

if __name__ == '__main__':
    main()
