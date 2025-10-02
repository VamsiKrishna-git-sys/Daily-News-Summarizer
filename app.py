import streamlit as st
from news_fetcher import fetch_news
from text_extractor import extract_full_text
from summarizer import summarize_text

st.set_page_config(page_title="Daily News Summarizer", layout="wide")

st.title("📰 Daily News Summarizer")
st.write("Fetches and summarizes the latest news for you!")

option = st.radio("Choose:", ["Top Headlines", "Search by Keyword"])
keyword = None
if option == "Search by Keyword":
    keyword = st.text_input("Enter keyword (e.g., AI, politics, sports)")

if st.button("Get Today's News"):
    with st.spinner("Fetching news..."):
        try:
            articles = fetch_news(keyword=keyword)
            if not articles:
                st.warning("No news found.")
            else:
                for art in articles:
                    headline = art["title"]
                    url = art["url"]
                    source = art["source"]["name"]

                    full_text = extract_full_text(url)
                    summary = summarize_text(full_text)

                    with st.container():
                        st.subheader(headline)
                        st.write(summary)
                        st.caption(f"Source: {source} | [Read more]({url})")
                        st.divider()

        except Exception as e:
            st.error(f"Something went wrong: {e}")
