import pathlib
import markdown
from pyscript import document, console

def load_article(event, article_id: str) -> str:
    """
    Loads Markdown Into article
    """
    article = document.querySelect(f"#{article_id}")
    article_path = pathlib.Path(f"{article_id}.md")
    if article_path.exists():
        article.innerHTML = markdown.markdown(article_path.read())
        
        
