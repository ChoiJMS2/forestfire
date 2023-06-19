import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime
from tqdm import tqdm
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

# 페이지 url 형식에 맞게 바꾸어 주는 함수 만들기
  #입력된 수를 1, 11, 21, 31 ...만들어 주는 함수
def makePgNum(num):
    if num == 1:
        return num
    elif num == 0:
        return num+1
    else:
        return num+9*(num-1)

# ConnectionError방지
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/98.0.4758.102"}

def run_crawling():
    news_df = []
    word = "강원도 산불"
    num = 0
    titles = []
    times = []
    medias = []
    contents = []
    columns = ['title','time','media','content']
    for i in range(1, 10):
        url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={word}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=28&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={i}"
        r = requests.get(url)
        b = BeautifulSoup(r.text, "html.parser")
        url_naver = b.select("div.group_news > ul.list_news > li div.news_area")

        for con in url_naver:
            title = con.select_one(".news_tit").text
            time = con.select_one("span.info").text
            media = con.select_one(".info.press").text
            content = con.select_one(".dsc_txt_wrap").text

            titles.append(title)
            times.append(time)
            medias.append(media)
            contents.append(content)

    return news_df

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