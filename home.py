# -*- coding:utf-8 -*-

import streamlit as st
from PIL import Image

def run_home():
    """
        Renders the introduction section of the app, including tabs for overview, objectives, and analysis phases.
    """
    tab1, tab2, tab3 = st.tabs([":desktop_computer: Introduction", ":trophy: Goals", ":bar_chart: Analysis "])
    with tab1:
        st.subheader(":white_check_mark: Project by")
        st.markdown(
            "Member|Skills|GitHub & Blog \n |:--:|:--:|:--:| \n |Beom-Mo Kim|-------- | ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/KingBeeM ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : -----| \n |Sang-Il Bae|------- | ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/BaeSang1 ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : https://tkddlf288.tistory.com/| \n |Yeol-Min Sung| -------| ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/YulminSung ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : https://muhanyuljung.tistory.com/ | \n |Sung-Jun Oh|------- | ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/sjohjun ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : https://djohjun.tistory.com/ | \n |Gwang-Hyeon Yim | -------|![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/Kwanghyun97/ ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) :  https://techtalkwithkwanghyun.tistory.com/manage | \n |Jae-Myoung Choi|------- | ![git](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FJVyru%2FbtseBexHPj3%2FVcOibIVPqoCkgLTA8mpP61%2Fimg.png) : https://github.com/ChoiJMS2m  ![blog](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftc61f%2FbtseGWwjM0C%2FD4Su9TE8awMKMdyhstKAO0%2Fimg.jpg) : https://james-choi88.tistory.com|")
        st.subheader(":white_check_mark: Project Calender")
        img = Image.open("img/wbs.png")
        st.image(img)

        st.subheader(":white_check_mark: Analytic Language & Tools")
        col1, col2, col3 = st.columns(3)
        with col1:
            img1 = Image.open("img/pycharm.png")
            st.image(img1, width=300)

        with col2:
            img2 = Image.open("img/python.png")
            st.image(img2, width=300)

        with col3:
            img3 = Image.open("img/streamlit.png")
            st.image(img3, width=300)
        col4, col5 = st.columns(2)
        with col4:
            img4 = Image.open("img/openapi.PNG")
            st.image(img4, width=450)
        with col5:
            img7 = Image.open("img/bigquery.png")
            st.image(img7, width=450)


    with tab2:
        st.subheader(":white_check_mark: 프로젝트 목표")
        img5 = Image.open("img/bp.png")
        st.image(img5)
        st.subheader(":white_check_mark: 주요 설정 지수")
        st.subheader(":white_check_mark: 평가 지표")

    with tab3:
        st.subheader(":white_check_mark: 프로젝트 순서도")
        img6 = Image.open("img/workflow.png")
        st.image(img6)

        st.subheader(":white_check_mark: 분석방향")

