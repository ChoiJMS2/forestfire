import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime
from tqdm import tqdm
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

def run_crawling():
    pass

def run_wordcloud():
    news_df = run_crawling()
    pass

def run_news():
    st.subheader("WordCloud")
    run_wordcloud()
    st.subheader("News")
    news_df = run_crawling()
    st.dataframe(news_df)

if __name__ == "__main__":
    run_news()