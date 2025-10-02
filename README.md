# 📰 Daily News Summarizer

The **Daily News Summarizer** is an AI-powered web application that fetches the latest news from reliable sources and provides concise summaries using advanced NLP models.  
Instead of reading lengthy articles, you can get quick, easy-to-read summaries highlighting the key points of each story.  

Built with **Streamlit**, **NewsAPI**, and **Hugging Face Transformers**.

---

## 🚀 Features
- Fetch **top headlines** or search news by keyword.
- Extract full article text using **newspaper3k** / **BeautifulSoup**.
- Generate short, clear summaries (4–5 sentences) using **BART**.
- Display results with headline, summary, source, and original link.
- Simple, interactive **Streamlit web interface**.

---

## 🛠️ Tech Stack
- **Language**: Python  
- **Framework**: Streamlit  
- **News API**: [NewsAPI.org](https://newsapi.org)  
- **Summarization Models**: Hugging Face Transformers (BART / T5)  
- **Libraries**: `requests`, `newspaper3k`, `beautifulsoup4`, `transformers`, `torch`  
- **Deployment**: Streamlit Cloud / Docker  

---

## 📂 Project Structure

daily-news-summarizer/
├── app.py # Main Streamlit app (UI + flow)

├── news_fetcher.py # Fetch news from NewsAPI

├── summarizer.py # Summarization functions

├── text_extractor.py # Extract full article text

├── requirements.txt # Dependencies


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/daily-news-summarizer.git
cd daily-news-summarizer

conda create -n news python=3.10 -y

conda activate news

pip install -r requirements.txt

streamlit run app.py
```
# 📸 Demo Screenshot

<img width="1706" height="706" alt="Screenshot 2025-10-02 215756" src="https://github.com/user-attachments/assets/831a310d-fc25-4f0b-8ac8-4fcc6d7e5cf3" />



