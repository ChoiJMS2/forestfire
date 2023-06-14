# -*- coding: utf-8 -*-
import streamlit as st
from service.news import run_news
from service.nowFire import run_nowFire
from service.fireStats import run_fireStats
from service.nowWarring import run_nowWarring
from service.callNumber import run_callNumber
from service.declaration import run_declaration

def run_service():
    st.sidebar.markdown("## SubMenu")
    Service_List = st.sidebar.radio(" ", ['News', '강원 비상 연락망', '신고 서비스', '현재 산불 상황', '현재 산불 위험 정보', '대형 산불 통계'], label_visibility='collapsed')
    if Service_List == 'News':
        st.header("강원 산불 뉴스")
        run_news()
    elif Service_List == '강원 비상 연락망':
        st.header("비상 연락망")
        run_callNumber()
    elif Service_List == '신고 서비스':
        st.header("신고 서비스")
        run_declaration()
    elif Service_List == '현재 산불 상황':
        st.header("현재 산불 상황")
        run_nowFire()
    elif Service_List == '현재 산불 위험 정보':
        st.header("현재 산불 위험 정보")
        run_nowWarring()
    elif Service_List == '대형 산불 통계':
        st.header("대형 산불 통계")
        run_fireStats()


if __name__ == "__main__":
    run_service()