from newspaper import Article
from bs4 import BeautifulSoup
import requests

def extract_full_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception:
        # Fallback with BeautifulSoup
        try:
            html = requests.get(url, timeout=5).text
            soup = BeautifulSoup(html, "html.parser")
            return " ".join([p.get_text() for p in soup.find_all("p")])
        except Exception:
            return ""
